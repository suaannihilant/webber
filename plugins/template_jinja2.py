# -*- coding: utf-8 -*-
import os
import types
import datetime
import webber

from webber import set_hook, cfg, functions

from jinja2 import Environment, FileSystemLoader


@set_hook('pagetemplate')
def pagetemplate(params):
    template_path = os.path.join(
        os.path.dirname(webber.__file__), cfg.style_dir
    )
    env = Environment(loader=FileSystemLoader(template_path))

    # Register filters
    for filter in filters:
        env.filters[filter.__name__] = filter

    template_filename = params.file.template
    if not template_filename.endswith('.html'):
            template_filename += '.html'
    template = env.get_template(template_filename)

    kw = {
        'file': params.file,
        'body': params.file.contents,
        'static_url': cfg.static_url
    }
    kw.update(params.file)
    kw.update(functions)

    rendered = template.render(**kw)
    return rendered

#
# Filters
#
# Jinja2 filter functions, add to `filters` list to have them automatically
# added to Jinja2 environment.
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    if type(value) is types.StringType:
        value = int(value)

    if type(value) in (types.IntType, types.LongType):
       value = datetime.datetime.fromtimestamp(value)
    return value.strftime(format)


filters = (
    datetimeformat,
)

