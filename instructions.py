#Requirements:
# 1. CSV file with GIS attributes, and values
#    All the CSV files should be places in the same folder as the 'json_sites.py' file.
# 2. One of the fields of the CSV should be named 'images'. All the image names should go in this column.
# 3. A number of jpg, png, bmp images that match the names in the 'images' column of the CSV.
#    The images should be placed in the folder 'static/images/NAME_OF_THE_PROJECT'

#Steps...
"""1. Create the JSON files that we will be using to parse the text and images for the slide show.
      The JSON file is a list of javascript objects."""
      # 1a. Make sure to place all the csv files in the same folder as the'json_sites.py' file. I placed this file in '/tools/'
      # 1b. Run the python files. The python file will automatically create a JSON file for every csv file in the folder.
      #     To run the file, cd into the '/tools/' folder. Once in the folder, type: 'python json_sites.py' on the command line.
      # 1c. If there are errors running the script it most likely has to do with a CSV files. The CSV library has sometimes problems
      #     with reading the excel generated CSVs. Copy the whole content of the csv file, paste it into a new document, and save it
      #     as a CSV again. Delete previous CSV files.
      # 1d. Move the newly created JSON files to the correct location. The location is: 'static/js/json'
      
"""2. Add the html elements to the DOM, these will load the images and call the necessary scripts"""
      # 2a. Move all the images to its proper location so the code can find them.
      #     You will have to create a folder with the name of the project: 'static/images/NAME OF THE PROJECT'
      #     Move all the images here
      
      # 2b. Copy and paste this on the html document:

        <!--This is where we define the slideshow divs, and call the script to replace the initial values-->
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        
        <div id="siteslides">
                <img class="siteimage" width="100%" src="static/images/LA/LA1_Page_002.jpg" alt="site design diagram"/>
                
                <div id="backwardtab"><</div>
                <div id="forwardtab">></div>
                        
                <div class="sitetext">
                        <p><span class="sitelabel">CLOSEST STREET:</span>
                        <!--<span class="sitesid">128</span>-->
                        <span class="street">Ventura</span></p>
                        
                        <p><span class="sitelabel">LOCAL WATERSHED:</span>
                        <span class="local">Bell Creek-Los Angeles River</span></p>
                        
                        <p><span class="sitelabel">MEDIUM WATERSHED:</span> 
                        <span class="medium">Upper Los Angeles River</span></p>
                        
                        <p><span class="sitelabel">REGIONAL WATERSHED:</span> 
                        <span class="regional">Los Angeles</span></p>
                        
                        <p><span class="sitelabel">GROUNDWATER BASIN:</span>
                        <span class="ground">Calabasas Creek</span></p>
                        
                        <p><span class="sitelabel">SOIL TYPE:</span>
                        <span class="soil">DIABLO CLAY LOAM</span></p> 
              </div>
        </div>
        
        <!-- This is the location of the script we will be using for the slideshow-->
        <script type="text/javascript" src="static/js/slideshowLA.js"></script>
    
      # 2b. We need to make a few changes to the code to reference the right information:
      #     First, we can only have one div with the same name... the script looks up the divs by id.
      #     Second, we need to change the location and name of the first image to show
      
        <div id="siteslides">#this sould have a number at the end to differentiate between them... ie <div id="siteslides3">
                # Here we need to change the location and name of the first image to show....
                <img class="siteimage" width="100%" src="static/images/NAME OF THE PROJECT/NAME OF THE FILE.jpg" alt="site design diagram"/>
                
      # 2c. We need to change the legend, and text associated with the particular project. We need to change the headings and then
      #     we need to change the values of the first site.
      #     Type the name and location of the script that will be doing the slideshow
      
                <div class="sitetext">
                        
                        # Here is where I define the heading or label of a particular GIS attribute
                        <p><span class="sitelabel">CLOSEST STREET:</span>
                        
                        # Here is where I manually type the values for the first site. We can get these values from the JSON file
                        <span class="street">Ventura</span></p>
                        
              </div>
              
        # Change the src location to the location of the new file, that is specific to this project
        <!-- This is the location of the script we will be using for the slideshow-->
        <script type="text/javascript" src="static/js/slideshowLA.js"></script>
      
      