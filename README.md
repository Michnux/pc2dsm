## Description of the Analytic:

A symplistic approach to generate a Digital Surface Model (DSM) (.tif) from a Point Cloud (.las)

The method to generate a DSM is the following:
- generate a raster from the .las taking the maximum z value of the point cloud at each point of the grid (supposedly the top of the trees)


## Inputs:

The PointCloud (.las) 


## Parameters:

The Grid Size: length (in m) of 1pix of the raster grid


## Outputs:

A raster file (.tif)
With the parametrized grid size
Categorized as 'DSM'


## Analytics creation

create_analytic.py allows to create the analytics without using the CLI
This requires credentials to be added to the project dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

Credentials to access the docker registry used still have to be created from the CLI


## Fix-me:

The scripts generates a raster (output.tif) as a final result.
A dataset is created and the output.tif component uplaoded from the docker using the SDK (cf. uplaod_dataset.py file)
This requires credentials to be added to the script_dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

this is a quick-fix as the transfert of the generated results (as described in the outputs.json file) doesn't seem to work properly
