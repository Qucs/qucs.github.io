qucs-web
========

Repository for the Qucs website.

[http://qucs.sourceforge.net/](http://qucs.sourceforge.net)

---

GitHub-Pages preview at:

[http://qucs.github.io/](http://qucs.github.io/)

---

Build:

The website is generated using [Pelican](https://blog.getpelican.com/) from the [reStructuredText](http://docutils.sourceforge.net/rst.html) sources in the directory `content/`.

Type `make html` to have the `html` pages generated in the `output/` directory.

Deploy:

 * Use the `deploy` script to upload the local repository to SourceForge
 * _Please push to the repository before uploading the website!_
 * Usage:

```
& ./deploy live [username]     #dry-run, SF password is requested
& ./deploy live go [username]  #upload with rsync over ssh, SF password is requested
```

Note:

 * Binary files currently hosted on the SourceForge website space were not added to this repository. TODO, move them elsewhere.
