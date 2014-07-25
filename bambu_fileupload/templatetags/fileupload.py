from django.template import Library, TemplateSyntaxError
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.importlib import import_module
from django.utils.http import urlencode
from django.core.urlresolvers import reverse
from django.utils.http import urlencode
from bambu_fileupload import DEFAULT_HANDLERS
from uuid import uuid4
import random, string

HANDLERS = dict(
    getattr(settings, 'FILEUPLOAD_HANDLERS', DEFAULT_HANDLERS)
)

register = Library()

@register.inclusion_tag('fileupload/styles.inc.html')
def fileupload_styles():
    return {}

@register.inclusion_tag('fileupload/scripts.inc.html')
def fileupload_scripts():
    return {}

@register.simple_tag(takes_context = True)
def fileupload_container(context, handler = 'attachments', callback_js = None, style = 'drag', **kwargs):
    if not handler in HANDLERS:
        raise TemplateSyntaxError('File uploaded handler %s not recognised' % handler)

    h = HANDLERS[handler]
    deletable = False
    listable = False

    if isinstance(h, (list, tuple)):
        h = list(h)
        func = h.pop(0)
        deletable = len(h) > 1
        listable = len(h) > 2

        if any(h) and not callback_js:
            callback_js = h.pop(0)
    else:
        func = h

    if not callback_js:
        callback_js = '(function(e) { window.location.href = document.location; })'

    module, dot, func = func.rpartition('.')

    try:
        module = import_module(module)
    except ImportError, ex:
        raise TemplateSyntaxError('Could not import module %s' % module, ex)

    try:
        func = getattr(module, func)
    except AttributeError, ex:
        raise TemplateSyntaxError(
            'Could not load handler %s from module %s' % (func, module.__name__), ex
        )

    if 'request' in context:
        request = context['request']
        if request.method == 'POST' and '_bambu_fileupload_guid' in request.POST:
            guid = request.POST['_bambu_fileupload_guid']
        else:
            guid = unicode(uuid4())
    else:
        guid = None

    if not any(kwargs):
        kwargs = dict(guid = guid)

    if not style in ('drag', 'button'):
        raise TemplateSyntaxError('style argument must be set to \'drag\' or \'button\'')

    container_id = 'bambu_fileupload_%s' % ''.join(random.sample(string.digits + string.letters, 6))
    script = """\n<script>\n//<![CDATA[\njQuery(document).ready(
        function($) {
            bambu.fileupload.init('%s','%s?%s', %s%s);
            %s
        }
    );\n//]]>\n</script>\n""" % (
        container_id,
        reverse('fileupload'),
        urlencode(
            {
                'handler': handler,
                'params': urlencode(kwargs)
            }
        ),
        callback_js,
        deletable and ", '%s?%s'" % (
            reverse('fileupload_delete'),
            urlencode(
                {
                    'handler': handler,
                    'params': urlencode(kwargs)
                }
            )
        ) or '',
        listable and (
            'bambu.fileupload.list(\'%s\', \'%s?%s\');' % (container_id,
                reverse('fileupload_list'),
                urlencode(
                    {
                        'handler': handler,
                        'params': urlencode(kwargs)
                    }
                )
            )
        ) or ''
    )

    if guid:
        script = u'<input name="_bambu_fileupload_guid" value="%s" type="hidden" />%s' % (guid, script)

    return render_to_string(
        'fileupload/%s.inc.html' % style,
        {
            'id': container_id,
            'guid': guid,
            'script': script,
            'style': style
        }
    )
