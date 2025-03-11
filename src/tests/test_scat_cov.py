import healpixml.scat_cov as scat_cov
import numpy as np

#=====================================================================================================================
# TEST Tensorflow version
#=====================================================================================================================

def test_tensorflow(nside=8):
    
    f=scat_cov.funct()
    
    im=np.random.randn(12*nside**2)
    im2=np.random.randn(12*nside**2)
    mask=np.ones([3,12*nside**2])
    
    assert np.isfinite(f.eval(im).flatten()).mean()==1
    assert np.isfinite(f.eval(im,image2=im2).flatten()).mean()==1
    assert np.isfinite(f.eval(im,image2=im2,mask=mask).flatten()).mean()==1
    




