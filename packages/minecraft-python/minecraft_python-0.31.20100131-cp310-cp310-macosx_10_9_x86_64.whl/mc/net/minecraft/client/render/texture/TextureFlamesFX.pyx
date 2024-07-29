# cython: language_level=3
# cython: cdivision=True, boundscheck=False, wraparound=False, nonecheck=False

from libc.string cimport memcpy

from mc.net.minecraft.client.render.texture.TextureFX cimport TextureFX
from mc.net.minecraft.game.level.block.Blocks import blocks
from mc.JavaUtils cimport random

cdef class TextureFlamesFX(TextureFX):

    cdef:
        float __currentFireFrame[320]
        float __lastFireFrame[320]

    def __init__(self, idx):
        TextureFX.__init__(self, blocks.fire.blockIndexInTexture + (idx << 4))
        for i in range(256):
            self.__currentFireFrame[i] = 0.0
            self.__lastFireFrame[i] = 0.0

    cpdef onTick(self):
        cdef int x, z, i, xx, zz, pixel, r, g, b, a, nr
        cdef float color
        cdef float frame[320]

        for x in range(16):
            for z in range(20):
                i = 18
                color = self.__currentFireFrame[x + ((z + 1) % 20 << 4)] * 18.0

                for xx in range(x - 1, x + 2):
                    for zz in range(z, z + 2):
                        if xx >= 0 and zz >= 0 and xx < 16 and zz < 20:
                            color += self.__currentFireFrame[xx + (zz << 4)]

                        i += 1

                self.__lastFireFrame[x + (z << 4)] = color / (i * 1.06)
                if z >= 19:
                    self.__lastFireFrame[x + (z << 4)] = random() * random() * \
                                                         random() * 4.0 + \
                                                         random() * 0.1 + 0.2

        memcpy(frame, self.__lastFireFrame, sizeof(self.__lastFireFrame))
        self.__lastFireFrame = self.__currentFireFrame
        self.__currentFireFrame = frame

        for pixel in range(256):
            color = self.__currentFireFrame[pixel] * 1.8
            if color > 1.0:
                color = 1.0

            if color < 0.0:
                color = 0.0

            r = <int>(color * 155.0 + 100.0)
            g = <int>(color * color * 255.0)
            b = <int>(color * color * color * color * color * color * color * color * color * color * 255.0)
            a = 0 if color < 0.5 else 255
            if self.anaglyphEnabled:
                nr = (r * 30 + g * 59 + b * 11) // 100
                g = (r * 30 + g * 70) // 100
                b = (r * 30 + b * 70) // 100
                r = nr

            self.imageData[pixel << 2] = <char>r
            self.imageData[(pixel << 2) + 1] = <char>g
            self.imageData[(pixel << 2) + 2] = <char>b
            self.imageData[(pixel << 2) + 3] = <char>a
