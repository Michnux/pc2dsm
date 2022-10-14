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

