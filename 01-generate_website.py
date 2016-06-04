wd = '/Users/danielmsheehan/GitHub/nyctreescountdatajam.github.com/map/'

varThemes = ['cttrees1995',
            'cttrees2005',
            'cttrees2015',
            'pctchact9505',
            'pctchact0515',
            'pctchact9515',
            'treesdn1995',
            'treesdn2005',
            'treesdn2015',
            'pctchadn9505',
            'pctchadn0515',
            'pctchadn9515'
            ]

varNames = ['Count Trees 1995 in Census Block 2010',
  'Count Trees 2005 in Census Block 2010',
  'Count Trees 2015 in Census Block 2010',
  'Percent Change in Count Trees 1995-2005 in Census Block 2010',
  'Percent Change in Count Trees 2005-2015 in Census Block 2010',
  'Percent Change in Count Trees 1995-2015 in Census Block 2010',
  'Tree Density per Square Mile 1995 in Census Block 2010',
  'Tree Density per Square Mile 2005 in Census Block 2010',
  'Tree Density per Square Mile 2015 in Census Block 2010',
  'Percent Change in Tree Density per Square Mile 1995-2005 in Census Block 2010',
  'Percent Change in Tree Density per Square Mile 2005-2015 in Census Block 2010',
  'Percent Change in Tree Density per Square Mile 1995-2015 in Census Block 2010'
            ]

vizIDs   = ['https://nygeog.cartodb.com/api/v2/viz/501f4b3e-2a86-11e6-9a28-0ecd1babdde5/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/8e0979c8-2a87-11e6-a159-0e3ff518bd15/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/c0dc2c10-2a87-11e6-852c-0e674067d321/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/f80c873e-2a87-11e6-a909-0e5db1731f59/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/7ff0a004-2a88-11e6-bd2d-0e787de82d45/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/9c739f1a-2a88-11e6-82a2-0e674067d321/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/249b6bca-2a89-11e6-852c-0e674067d321/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/42780770-2a89-11e6-9b0e-0ecfd53eb7d3/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/5be136a0-2a89-11e6-8388-0e5db1731f59/viz.json',

            'https://nygeog.cartodb.com/api/v2/viz/c1b32340-2a88-11e6-8031-0ea31932ec1d/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/ec0f6d06-2a88-11e6-8d58-0ecfd53eb7d3/viz.json',
            'https://nygeog.cartodb.com/api/v2/viz/074fe1c2-2a89-11e6-94e1-0ecd1babdde5/viz.json']
   
api_pre = 'https://nygeog.cartodb.com/api/v2/sql?filename=nycb2010_treesdata_'

# theVars = [['t10km2','t10lndkm2','t10cnt','t10resdn1','t10intden','t10entrpy','t10rtlfar','t10sub07d','t10walk','t10walkc'],
#            ['t10treepc'],
#            ['t10birtlen'],
#            ['t10mhhi'],
#            ['t10totpop'],
#            ['t10popdens'],
#            ['t10pcag65u'],
#            ['t10pcpov'],
#            ['t10pcblack'],
#            ['t10pcasian'],
#            ['t10pcunemp'],
#            ['t10muc0311'],
# #            ['t10mur0311'],
#            ['t10pek9513'],
#            ['t10pei9513'],
#            ['t10bik9513'],
#            ['t10bii9513'],
#            ['t10cntcafe'],
#            ['t10alcelig','t10alcall','t10alccl1','t10alccl2','t10alccl3','t10alccl4','t10alccl5'],
# #            ['t10subctdo']
#            ]    

theVars = [['count1995'],
  ['count2005'],
  ['count2015'],
  ['pctchange95_05'],
  ['pctchange05_15'],
  ['pctchange95_15'],
  ['treedensqmi1995'],
  ['treedensqmi2005'],
  ['treedensqmi2015'],
  ['pctchange95_05trdn'],
  ['pctchange05_15trdn'],
  ['pctchange95_15trdn']]

dropdownStuff = []

for i, varTheme, varName in zip(range(19), varThemes, varNames):
    if i == 0:
        preHtmlText = '' #'<strong>Built Environment</strong>'
    elif i == 3:
        preHtmlText = '' #'<strong>Social Environment</strong>'
    elif i == 11:
        preHtmlText = '' #'<strong>Safety</strong>'
    elif i == 16:
        preHtmlText = '' #'<strong>Businesses Environment</strong>'
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
            <button class="btn btn-default dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Variables
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
          <button onclick='location.href="'''+api_pre+csvUrl+'''"'><strong>Export</strong> '''+varName+''' data as <strong>CSV</strong></button>
          <p></p>
          <button onclick='location.href="'''+api_pre+shpUrl+'''"'><strong>Export</strong> '''+varName+''' data as <strong>Shapefile</strong></button>
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
        zoom: 11,
        layers: [toggler]
      })
      //L.tileLayer('https://dnv9my2eseobd.cloudfront.net/v3/cartodb.map-4xtxp73f/{z}/{x}/{y}.png', {
      //  attribution: 'Mapbox <a href="http://mapbox.com/about/maps" target="_blank">Terms &amp; Feedback</a>'
      //}).addTo(map);
      //L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      //    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      //}).addTo(map);
      L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
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