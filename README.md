qucs-web
========

Repository for the Qucs website.

[http://qucs.sourceforge.net/](http://qucs.sourceforge.net)

---

GitHub-Pages preview at:

[http://qucs.github.io/](http://qucs.github.io/)

---

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
