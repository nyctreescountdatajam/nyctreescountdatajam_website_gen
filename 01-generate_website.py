wd = '/Users/danielmsheehan/GitHub/nyctreescountdatajam.github.com/map/'

varThemes = ['cttrees1995',
            'cttrees2005',
            'cttrees2015',
            'treesdn1995',
            'treesdn2005',
            'treesdn2015',
            'pctchange9505den',
            'pctchange0515den',
            'pctchange9515den',
            'pctchange9515den_tree_million',
            'all_trees_1995_2005_2015',
            'treescon2015',
            ]

varNames = ['Count Trees <strong>1995</strong> in Census Block',
  'Count Trees <strong>2005</strong> in Census Block',
  'Count Trees <strong>2015</strong> in Census Block',
  'Tree Count Density <strong>1995</strong> per Square Mile in Census Block',
  'Tree Count Density <strong>2005</strong> per Square Mile in Census Block',
  'Tree Count Density <strong>2015</strong> per Square Mile in Census Block',
  'Percent Change in Tree Count Density <strong>1995 -> 2005</strong> per Square Mile in Census Block',
  'Percent Change in Tree Count Density <strong>2005 -> 2015</strong> per Square Mile in Census Block',
  'Percent Change in Tree Count Density <strong>1995 -> 2015 (20 years)</strong> per Square Mile in Census Block',
  'Percent Change in Tree Count Den. <strong>1995 -> 2015</strong> per Sq. Mi. in Cen. Blk. w/ Counts',
  'Street Tree Census 1995-2005-2015',
  'Street Tree Conditions 2015'
            ]

vizIDs   = ['https://nygeog.cartodb.com/api/v2/viz/285d1c84-2dba-11e6-8a62-0ea31932ec1d/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/f4d493dc-2dba-11e6-96db-0e31c9be1b51/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/2fb72b68-2dbb-11e6-a428-0e5db1731f59/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/8f680cd0-2dbb-11e6-9c65-0ea31932ec1d/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/710e5c98-2dbc-11e6-92cc-0e674067d321/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/f5811e84-2dbc-11e6-9998-0ecfd53eb7d3/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/ca8aced6-2dbd-11e6-bf76-0e5db1731f59/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/9e04739c-2dbf-11e6-b7d7-0e31c9be1b51/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/1760d3e8-2dc0-11e6-92cc-0e674067d321/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/701fd574-2dc0-11e6-8a62-0ea31932ec1d/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/fc8e830c-2e3d-11e6-a126-0ecfd53eb7d3/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/55c4d968-3243-11e6-8f80-0ecfd53eb7d3/viz.json']
   
api_pre = 'https://nygeog.cartodb.com/api/v2/sql?filename=nycb2010_treesdata_'


theVars = [['count1995'],
  ['count2005'],
  ['count2015'],
  ['treedensqmi1995'],
  ['treedensqmi2005'],
  ['treedensqmi2015'],
  ['pctchange9505den'],
  ['pctchange0515den'],
  ['pctchange9515den'],
  ['count1995','count2015','pctchange9515den'],
  ['count1995','count2005','count2015'],
  ['count1995','count2005','count2015'] #replace w/ conditions
  ]

dropdownStuff = []

for i, varTheme, varName in zip(range(19), varThemes, varNames):
    if i == 0:
        preHtmlText = '<strong> Count Trees</strong>'
    elif i == 3:
        preHtmlText = '<strong> Tree Density (trees per square mile)</strong>'
    elif i == 6:
        preHtmlText = '<strong> Percent Change in Tree Density (trees per square mile)</strong>'
    elif i == 9:
        preHtmlText = '<strong> Percent Change in Tree Density (trees per square mile) with Counts of Trees</strong>'
    elif i == 10:
        preHtmlText = '<strong>Street Tree Census 1995-2005-2015</strong>'
    elif i == 11:
        preHtmlText = '<strong>Street Tree Conditions</strong>'
    else:
        preHtmlText = '' #''
    htmlText = preHtmlText + '<li role="presentation"><a href="'+varTheme+'.html" id="'+varTheme+'" class="button '+varTheme+'">'+varName+'</a></li>' 
    dropdownStuff.append(htmlText)
    
dropdownHTML = ''.join(dropdownStuff) 
print dropdownHTML
              
for theVar, varTheme,varName,vizID in zip(theVars,varThemes,varNames,vizIDs):
    csvUrl = varTheme.replace('-','_') + '.csv&format=csv&q=SELECT bctcb2010,' + ','.join(theVar) +  ' FROM nycb2010_treesdata'
    shpUrl = varTheme.replace('-','_') + '&format=shp&q=SELECT the_geom,bctcb2010,' + ','.join(theVar) +  ' FROM nycb2010_treesdata'
    
    dictUrl = '../../../data/dictionary/'+varTheme+'.html'
    
    
    html_str = '''<html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
      <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
      <link rel="stylesheet" href="http://libs.cartocdn.com/cartodb.js/v3/3.11/themes/css/cartodb.css" />
      <script src="http://libs.cartocdn.com/cartodb.js/v3/3.11/cartodb.js"></script>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
      <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    
      <link rel="stylesheet" href="css/style.css">   <!-- LOCAL FILE -->
      <script src="js/'''+varTheme+'''_script.js"></script>   <!-- LOCAL FILE -->
    </head>
    
    <body onload="init()">
      <div id='map'></div>
      <!-- LEFT PANEL IS SAME FOR EVERY PAGE -->
      <div id="leftpanel">

        <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="../../../" class="button all">Home</a>
            </button>
        <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="https://nygeog.cartodb.com/tables/nycb2010_treesdata/public" class="button all">All Data</a>
            </button>
        <button class="btn btn-default dropdown-toggle" type="button" id="menu1"><a href="" class="button all">Reset</a>
            </button>
    
          <div class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Street Tree Census 1995-2015 Counts & Density by Census Block
            <span class="caret"></span></button>
            <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">
              '''+dropdownHTML+'''
            </ul>
          </div>
        </div>
      </div>
      <!-- LEFT PANEL IS SAME FOR EVERY PAGE -->
      <div id='exports'>
          
          <!-- <button onclick='location.href="'''+dictUrl+'''"'>'''+varName+''' <strong>Data dictionary</strong></button> -->
          <p></p>
          <p></p>
          <button onclick='location.href="'''+api_pre+csvUrl+'''"'>Export '''+varName+''' data as <strong>CSV</strong></button>
          <p></p>
          <button onclick='location.href="'''+api_pre+shpUrl+'''"'>Export '''+varName+''' data as <strong>Shapefile</strong></button>
       </div>
       <!-- ALL DATA PANEL IS OFF - SEE LEFTPANEL
       <div id='alldata'>
          <p></p>
          <button onclick='location.href="../../../data/download.html"'>Download master data</button>
       </div> -->
    </body>
    </html>'''
    
    
    Html_file= open(wd+varTheme+'.html',"w")
    Html_file.write(html_str)
    Html_file.close()
    

for varTheme,varName,vizID in zip(varThemes,varNames,vizIDs):
    js_str = '''var map;
        function init(){
        
      var toggler = new L.LayerGroup();
      // initiate leaflet map
      map = new L.Map('map', { 
        center: [40.705,-74.00], 
        zoom: 12,
        layers: [toggler]
      })
      //L.tileLayer('https://dnv9my2eseobd.cloudfront.net/v3/cartodb.map-4xtxp73f/{z}/{x}/{y}.png', {
      //  attribution: 'Mapbox <a href="http://mapbox.com/about/maps" target="_blank">Terms &amp; Feedback</a>'
      //}).addTo(map);
      //L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      //    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      //}).addTo(map);
      L.tileLayer('http://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
        }).addTo(map);

    
      var layerUrl = "'''+vizID+'''";
    
      var sublayers = [];
    
      cartodb.createLayer(map, layerUrl,{
                title: true,
                description: false,
                search: true,
                tiles_loader: true,
                layer_selector:true,
                cartodb_logo: false,
                legends: true
            })
      .addTo(map)
      .addTo(toggler)
      .on('done', function(layer) {
        // change the query for the first layer
        var subLayerOptions = {
          //sql: "SELECT * FROM ne_10m_populated_places_simple",
          //cartocss: "#ne_10m_populated_places_simple{marker-fill: #F84F40; marker-width: 8; marker-line-color: white; marker-line-width: 2; marker-clip: false; marker-allow-overlap: true;}"
        }
    
        var sublayer = layer.getSubLayer(0);
    
        sublayer.set(subLayerOptions);
    
        sublayers.push(sublayer);
      }).on('error', function() {
        //log the error
      });
      var baseLayers = {
        //turned off just so can add to L.control.layers
      };

      var overlays = {
        "'''+varName+''' Layer On/Off": toggler
      };

      L.control.layers(baseLayers, overlays).addTo(map);
    }'''

    Html_file= open(wd+'js/'+varTheme+'_script.js',"w")
    Html_file.write(js_str)
    Html_file.close()