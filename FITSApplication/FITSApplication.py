
from astropy.io import fits
hdul = fits.open('D:\OneDrive\Kepler-data\kplr000757076-2009131105131_llc.fits')
hdul.info()
print('==========')
hdr = hdul[0].header
print(repr(hdr))
print('==============')
print(list(hdr.keys()))
