
function header()
{
  // Multiline header string
  var string = '\
  <!-- comon qucs header --> \
  <div id="header"></div> \
  <div id="navpane" class="nav"> \
    <ul class="nav"> \
      <li><a class="navbutton" href="index.html">home</a></li> \
      <li><a class="navbutton" href="screenshots.html">screenshots</a></li> \
      <li><a class="navbutton" href="docs.html">support</a><li> \
      <li><a class="navbutton" href="download.html">download</a></li> \
      <li><a class="navbutton" href="road.html">roadmap</a></li> \
      <li><a class="navbutton" href="devs.html">developers</a></li> \
      <li><a class="navbutton" href="faq.html">FAQ</a></li> \
      <li><a class="navbutton" href="contact.html">contact</a></li> \
    </ul> \
  </div>';

  // Write content
  document.write(string);
}


function footer()
{
  // Multiline footer string
  var string = '\
  <!-- common footer element for qucs web pages --> \
  <div id="footer"> \
    <center> \
      &copy; 2004 -- 2013 Qucs team \
    </center> \
  </div>'

  // Write content
  document.write(string);
}


