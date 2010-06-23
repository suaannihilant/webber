# -*- coding: iso-8859-1 -*-
from webber import *
import os, datetime
try:
	import PyRSS2Gen
except ImportError:
	print "rss_feed needs the python module PyRSS2Gen"
	raise

items = []


@set_hook("checkconfig")
def checkconfig(params):
	if not cfg.has_key("rss_file"):
		log('no "rss_file:" configured, using "feed.rss":', 4)
		cfg.rss_file = "feed.rss"


ZERO = datetime.timedelta(0)

class UTC(datetime.tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO
utc = UTC()


@set_hook("scan")
def sitemap_scan(params):
	global items

	file = params.file
	if not file.has_key("linktitle"):
		return
	if not file.has_key("change"):
		return

	fname_out = os.path.join(cfg.out_dir, file.out_path)
	full_url = "http://%s/%s" % (cfg.main_url, fname_out)
	item = PyRSS2Gen.RSSItem(
		title = file["title"],
		link = full_url,
		guid = PyRSS2Gen.Guid("%s %s" % (full_url, file["mtime"])),
		description = file["change"],
		pubDate = datetime.datetime.fromtimestamp(file["mtime"], utc),
	)
	items.append(item)



@set_hook("finish")
def finish(params):
	rss = PyRSS2Gen.RSS2(
		title = cfg.subtitle,
		link = "http://%s" % cfg.main_url,
		description = cfg.subtitle,
		lastBuildDate = datetime.datetime.now(),
		items = items,
	)
	try:
		os.makedirs(cfg.out_dir)
	except:
		pass
	rss.write_xml( open(os.path.join(cfg.out_dir, cfg.rss_file), "w"))