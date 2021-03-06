title: Plugins
parent: Webber
lang: en
ctime: 2009-06-26
mtime: 2010-04-16

Webber doesn't do much on it's own. Almost all the real work is delegated
to plugins. Those plugins do:

* Read files and generate HTML snippets ([[read_rst.py|read_rst]],
  [[read_markdown.py|read_markdown]], [[read_html.py|read_html]])
  or copy files verbatim, e.g. for graphics
  ([[read_copyonly.py|read_copyonly]])
* Update internal state or modify HTML snippets
  ([[hierarchy.py|hierarchy]], [[link.py|link]])
* Create HTML pages ([[template_mako.py|template_mako]])
* Create additional output files ([[google_sitemap.py|google_sitemap]])

There's another plugin there ([[skeleton.py|skeleton]]), which is
is just a demo for plugin-programmers.

Plugins simply reside in the "`plugins/`" directory from webber itself. If your
web project needs local plugins, you can specify additional plugins with
"`plugin_dirs`" in [[webber.conf|configuration]].

Note that webber doesn't load all of them automatically. Instead you specify
in the configuration file [[webber.conf|configuration]] which plugins you
want. Use the variable "`plugins`" for that.

Once plugins are loaded, webber orchestrates the work of itself and
all plugins via [[hooks]].
