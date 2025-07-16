// Define AOI (Mukuru Region, Nairobi)
var geometry = ee.Geometry.Rectangle([36.8655, -1.323, 36.8945, -1.300]);
Map.centerObject(geometry, 14);

// Load Sentinel-2 Image Collection (use Level-2A for surface reflectance)
var s2 = ee.ImageCollection('COPERNICUS/S2_SR')
  .filterBounds(geometry)
  .filterDate('2024-02-01', '2024-03-01')  // Change date as needed
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 9
  ))  // Keep low-cloud images
  .median()  // Reduce to one image by median

// Select RGB bands (B4 = Red, B3 = Green, B2 = Blue)
var rgb = s2.select(['B4', 'B3', 'B2']).clip(geometry);

// Visualization parameters
var visParams = {
  bands: ['B4', 'B3', 'B2'],
  min: 0,
  max: 3000
};

// Display RGB image
Map.addLayer(rgb, visParams, 'Sentinel-2 RGB Mukuru');

// Export RGB image to Google Drive
Export.image.toDrive({
  image: rgb,
  description: 'Mukuru_RGB_Sentinel2',
  folder: 'GEE_Exports',
  fileNamePrefix: 'Mukuru_RGB_2024',
  region: geometry,
  scale: 10,
  maxPixels: 1e9
});
