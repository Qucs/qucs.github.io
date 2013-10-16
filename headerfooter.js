
function header()
{
  // Multiline header string
  var string = '\
  <!-- comon qucs header --> \
  <div id="header"></div> \
  <div id="navpane" class="nav"> \
    <ul class="nav"> \
      <li><a class="navbutton" href="index.shtml">home</a></li> \
      <li><a class="navbutton" href="screenshots.shtml">screenshots</a></li> \
      <li><a class="navbutton" href="docs.shtml">support</a><li> \
      <li><a class="navbutton" href="download.shtml">download</a></li> \
      <li><a class="navbutton" href="road.shtml">roadmap</a></li> \
      <li><a class="navbutton" href="devs.shtml">developers</a></li> \
      <li><a class="navbutton" href="faq.shtml">FAQ</a></li> \
      <li><a class="navbutton" href="contact.shtml">contact</a></li> \
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


