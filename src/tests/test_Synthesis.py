import healpixml.scat_cov as scat_cov
import healpixml.Synthesis as synthe
import numpy as np

#=====================================================================================================================
# TEST Tensorflow version
#=====================================================================================================================

def test_tensorflow(nside=8):
    
    f=scat_cov.funct()
    
    im=np.random.randn(12*nside**2)
    
    # Compute the reference statistics and store the normalization in *scat_op*
    ref = f.eval(im, norm='auto')

    # Recompute the coefficients using the stored normalization in *scat_op* (norm='self')
    ref, sref = f.eval(im, calc_var=True, norm='self')
    
    def The_loss_mean(u, scat_operator, args):
        ref  = args[0]
        sref = args[1]
        
        # Compute the mean scattering covariance of the current synthesized maps called u
        learn = scat_operator.reduce_mean_batch(scat_operator.eval(u, norm='self'))
        # Compute the difference with the reference coefficients
        loss = scat_operator.reduce_mean(scat_operator.square((learn - ref) / sref))

        return loss

    loss_mean = synthe.Loss(The_loss_mean, f, ref, sref)

    sy_mean = synthe.Synthesis([loss_mean])

    # Initialize 4 images: Changing this value will generate an ensemble of the specified number of images (here 4).
    imap = np.random.randn(4, 12 * nside**2) * np.std(im)

    omap = f.to_numpy(sy_mean.run(imap,   
                        EVAL_FREQUENCY=1,
                        NUM_EPOCHS=10))
                        
    assert  np.isfinite(omap).mean()==1
    




