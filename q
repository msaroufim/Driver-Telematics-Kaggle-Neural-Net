<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>Home</title>
    <link rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon.ico?v=30780f272ab4aac64aa073a841546240">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=60f0405edd95e7135ec6a0bbc36d1385" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="/static/style/style.min.css?v=3938f8554ee5d9c06ee2fb644a20bec4" type="text/css"/>
    
    <link rel="stylesheet" href="/static/custom/custom.css?v=900035aa0c126bb85df55c5b3e51b6f1" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/requirejs/require.js?v=640929dac3c23a448d2eebc37bc32062" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20150613014329",
          
          baseUrl: '/static/',
          paths: {
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jquery: 'components/jquery/jquery.min',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            jqueryui: 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/moment',
            codemirror: 'components/codemirror',
            termjs: 'components/term.js/src/term',
          },
          shim: {
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            jqueryui: {
              deps: ["jquery"],
              exports: "$"
            }
          }
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });
    </script>

    
    

</head>

<body class="" 

data-base-url="/"
data-notebook-path=""
data-terminals-available="True"

>

<noscript>
    <div id='noscript'>
      IPython Notebook requires JavaScript.<br>
      Please enable it to proceed.
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand pull-left"><a href="/tree" title='dashboard'><img src='/static/base/images/logo.png?v=7c4597ba713d804995e8f8dad448a397' alt='Jupyter Notebook'/></a></div>

  

  

    <span id="login_widget">
      
    </span>

  

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="#running" data-toggle="tab">Running</a></li>
        <li><a href="#clusters" data-toggle="tab">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" class="duplicate-button btn btn-default btn-xs">Duplicate</button>
                  <button title="Rename selected" class="rename-button btn btn-default btn-xs">Rename</button>
                  <button title="Shutdown selected notebook(s)" class="shutdown-button btn btn-default btn-xs btn-warning">Shutdown</button>
                  <button title="Deleted selected" class="delete-button btn btn-default btn-xs btn-danger"><i class="fa fa-trash"></i></button>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id='alternate_upload'  class='alternate_upload'>
                  <span id="notebook_list_info">
                  <span class="btn btn-xs btn-default btn-upload">
                  <input  title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple='multiple'>
                  Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu">
                    <li role="presentation" id="new-file">
                      <a role="menuitem" tabindex="-1" href="#">Text File</a>
                    </li>
                    <li role="presentation" id="new-folder">
                      <a role="menuitem" tabindex="-1" href="#">Folder</a>
                    </li>
                    
                    <li role="presentation" id="new-terminal">
                      <a role="menuitem" tabindex="-1" href="#">Terminal</a>
                    </li>
                    
                    <li role="presentation" class="divider"></li>
                    <li role="presentation" class="dropdown-header" id="notebook-kernels">Notebooks</li>
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" type="button" class="btn btn-default btn-xs" id="button-select-all">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all"><span id="counter-select-all">&nbsp;</span></input>
                </button>
                <button title="Select..." class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id='selector-menu' class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="presentation"><a id="select-folders" role="menuitem" tabindex="-1" href="#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i> Folders</a></li>
                  <li role="presentation"><a id="select-notebooks" role="menuitem" tabindex="-1" href="#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i> All Notebooks</a></li>
                  <li role="presentation"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i> Running</a></li>
                  <li role="presentation"><a id="select-files" role="menuitem" tabindex="-1" href="#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i> Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb">
                  <li><a href="/tree"><i class="fa fa-home"></i></a></li>
                
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right">
              <button id="refresh_running_list" title="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion" >
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="#">
                  Terminals
                </a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list">
                    <div id="terminal_list_header" class="row list_placeholder">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="#">
                  Notebooks
                </a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list">
                    <div id="running_list_placeholder" class="row list_placeholder">
                      <div> There are no notebooks running. </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>   
        </div>
        <div id="clusters" class="tab-pane">
          <div id="cluster_toolbar" class="row">
            <div class="col-xs-8 no-padding">
              <span id="cluster_list_info">IPython parallel computing clusters</span>
            </div>
            <div class="col-xs-4 no-padding tree-buttons">
              <span id="cluster_buttons" class="pull-right">
              <button id="refresh_cluster_list" title="Refresh cluster list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div id="cluster_list">
            <div id="cluster_list_header" class="row list_header">
              <div class="profile_col col-xs-4">profile</div>
              <div class="status_col col-xs-3">status</div>
              <div class="engines_col col-xs-3" title="Enter the number of engines to start or empty for default"># of engines</div>
              <div class="action_col col-xs-2">action</div>
            </div>
          </div>
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content --> 
  </div><!-- ipython-main-app  -->


</div>





    


<script src="/static/tree/js/main.js?v=fc3bc3575dcf76dc18c8ec12c4a838da" type="text/javascript" charset="utf-8"></script>


</body>

</html>