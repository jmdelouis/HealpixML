import sys

import tensorflow as tf


class healpixml_backend_tens:

    def __init__(self, backend):

        self.bk = backend

    # ---------------------------------------------−---------

    @tf.function
    def loss(self, x, batch, loss_function):

        operation = loss_function.scat_operator

        nx = 1
        if len(x.shape) > 1:
            nx = x.shape[0]

        with tf.device(
            operation.gpulist[(operation.gpupos + self.curr_gpu) % operation.ngpu]
        ):
            print(
                "%s Run %d [PROC=%04d] on GPU %s"
                % (
                    loss_function.name,
                    loss_function.id_loss,
                    self.mpi_rank,
                    operation.gpulist[
                        (operation.gpupos + self.curr_gpu) % operation.ngpu
                    ],
                )
            )
            sys.stdout.flush()

            l_x = x
            """
            if nx>1:
                l_x={}
            for i in range(nx):
            """

            if nx == 1:
                ndata = x.shape[0]
            else:
                ndata = x.shape[0] * x.shape[1]

            if self.KEEP_TRACK is not None:
                l_loss, linfo = loss_function.eval(l_x, batch, return_all=True)
            else:
                l_loss = loss_function.eval(l_x, batch)

            g = tf.gradients(l_loss, x)[0]
            g = self.backend.check_dense(g, ndata)
            self.curr_gpu = self.curr_gpu + 1

        if self.KEEP_TRACK is not None:
            return l_loss, g, linfo
        else:
            return l_loss, g
