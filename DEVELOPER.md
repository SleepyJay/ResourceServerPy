# ResourceServerPy - Developer Notes

## Various notes about design decisions

#### 1. Using `/$/` in Classpaths

This was originally written to pull in JavaScript files. We allowed a emitter option to output which files were pulled in and also another emitter option that would actually produce `<script>` tags. In both cases, we want paths that are relative to a docroot, which was presumably only a portion of the physical disk location of a file. 

So we used to have a directive, `rewrite`, which would take a regex and value. Then each rewrite regex would be run against every resource path using a substitution with the given value. For instance, if you had a resource in the path `/home/sleepjay/projects/web/htdocs/js/Foo.js` you would want only `js/Foo.js` to show up as the source of the resource. Thus, you would write `//@ rewrite /home/sleepjay/projects/web/htdocs/ => ""` which would simply remove any paths that started with that. 

This seemed reasonable enough to me. And, we usually didn't need to do the regexing for production code, so any (minor) performance hits were irrelevant.
However, some users seemed a little confused by it. And, indeed, most of the time (not all) you would only be **removing** parts, not setting new ones. 

So, the `/$/` now separates the "physical location" from the "docroot" location. Eventually, I may allow the classpath to be smarter.
