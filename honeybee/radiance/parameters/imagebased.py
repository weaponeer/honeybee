"""Radiance raytracing Parameters."""
from ._advancedparametersbase import AdvancedRadianceParameters
from ._defaultset import rpict_number_parameters, rpict_boolean_parameters
from ._frozen import frozen


# TODO: Implement additional Rad Parameters
# @mostaphaRoudsari I think this TODO is done.

@frozen
class ImageBasedParameters(AdvancedRadianceParameters):
    """Radiance Parameters for generating images.

    Attributes:
        quality: An integer between 0-2 (0:low, 1: medium or 2: high quality)
        ambientBounces: Number of ambient bounces. This is the maximum number of diffuse
            bounces computed by the indirect calculation. A value of zero
            implies no indirect calculation.
        ambientDivisions: Number of ambient divisions. The error in the Monte Carlo calculation
            of indirect illuminance will be inversely proportional to the square
            root of this number. A value of zero implies no indirect calculation.
        ambientSupersamples: Number of ambient super-samples. Super-samples are applied only to
            the ambient divisions which show a significant change.
        ambientResolution: Number of ambient resolution. This number will determine the maximum
            density of ambient values used in interpolation. Error will start to
            increase on surfaces spaced closer than the scene size divided by the
            ambient resolution. The maximum ambient value density is the scene
            size times the ambient accuracy.
        ambientAccuracy: Number of ambient accuracy. This value will approximately equal the
            error from indirect illuminance interpolation. A value of zero
            implies no interpolation

        for the full list of attributes try self.keys

    Usage:

        rp = ImageBasedParameters(0)
        print rp.toRadString()

        > -aa 0.25 -ab 2 -ad 512 -dc 0.25 -st 0.85 -lw 0.05 -as 128 -ar 16 -lr 4 -dt 0.5 -dr 0 -ds 0.5 -dp 64

        rp = ImageBasedParameters(1)
        print rp.toRadString()

        > -aa 0.2 -ab 3 -ad 2048 -dc 0.5 -st 0.5 -lw 0.01 -as 2048 -ar 64 -lr 6 -dt 0.25 -dr 1 -ds 0.25 -dp 256

        rp = ImageBasedParameters(2)
        print rp.toRadString()
        > -aa 0.1 -ab 6 -ad 4096 -dc 0.75 -st 0.15 -lw 0.005 -as 4096 -ar 128 -lr 8 -dt 0.15 -dr 3 -ds 0.05 -dp 512

        rp.ab = 5
        rp.u = True
        print rp.toRadString()

        > -aa 0.1 -ab 5 -dj 0.7 -ad 4096 -dc 0.75 -st 0.15 -lw 0.005 -as 4096 -ar 128 -lr 8 -dt 0.15 -dr 3 -ds 0.05 -dp 512 -u
    """

    def __init__(self, quality=None, ambientBounces=None, ambientDivisions=None,
                 ambientSupersamples=None, ambientResolution=None, ambientAccuracy=None,
                 directJitter=None, directSampling=None, directThreshold=None,
                 directCertainty=None, directSecRelays=None, directPresampDensity=None,
                 specularThreshold=None, limitWeight=None, limitReflections=None,
                 specularSampling=None,  uncorRandSamp=None, pixelSampling=None,
                 pixelJitter=None,pixelTolerance=None,pixelAspectRatio=None,
                 pixelMotionBlur=None,pixelDepthOfField=None,ambientValue=None,
                 ambientWeight=None,directVisibility=None,backFaceVisibility=None ):
        """Create Radiance paramters."""
        AdvancedRadianceParameters.__init__(self)
        self.quality = quality
        """An integer between 0-2 (0:low, 1: medium or 2: high quality)"""

        self.addRadianceNumber('ab', descriptiveName='ambient bounces',
                               attributeName="ambientBounces", numType=int)
        self.ambientBounces = ambientBounces
        """ Number of ambient bounces. This is the maximum number of diffuse
            bounces computed by the indirect calculation. A value of zero
            implies no indirect calculation."""

        self.addRadianceNumber('ad', descriptiveName='ambient divisions',
                               attributeName="ambientDivisions", numType=int)
        self.ambientDivisions = ambientDivisions
        """ Number of ambient divisions. The error in the Monte Carlo calculation
            of indirect illuminance will be inversely proportional to the square
            root of this number. A value of zero implies no indirect calculation.
        """

        self.addRadianceNumber('as', descriptiveName='ambient super samples',
                               attributeName='ambientSupersamples', numType=int)
        self.ambientSupersamples = ambientSupersamples
        """ Number of ambient super-samples. Super-samples are applied only to
            the ambient divisions which show a significant change.
        """

        self.addRadianceNumber('ar', descriptiveName='ambient resolution',
                               attributeName='ambientResolution', numType=int)
        self.ambientResolution = ambientResolution
        """ Number of ambient resolution. This number will determine the maximum
            density of ambient values used in interpolation. Error will start to
            increase on surfaces spaced closer than the scene size divided by the
            ambient resolution. The maximum ambient value density is the scene
            size times the ambient accuracy."""

        self.addRadianceNumber('aa', descriptiveName='ambient accuracy',
                               attributeName='ambientAccuracy', numType=float)
        self.ambientAccuracy = ambientAccuracy
        """Number of ambient accuracy. This value will approximately equal the
        error from indirect illuminance interpolation. A value of zero implies
        no interpolation."""

        self.addRadianceNumber('dj', descriptiveName='direct source jitter',
                               attributeName='directJitter', numType=float)
        self.directJitter = directJitter
        """
        -dj frac
        Set the direct jittering to frac. A value of zero samples each source
        at specific sample points (see the -ds option below), giving a smoother
        but somewhat less accurate rendering. A positive value causes rays to
        be distributed over each source sample according to its size,
        resulting in more accurate penumbras. This option should never be
        greater than 1, and may even cause problems (such as speckle)when the
        value is smaller. A warning about aiming failure will issued if frac is
        too large. It is usually wise to turn off image sampling when using
        direct jitter by setting -ps to 1.
        """

        self.addRadianceNumber('ds', descriptiveName='direct sampling',
                               attributeName='directSampling', numType=float)
        self.directSampling = directSampling
        """
        -ds frac
        Set the direct sampling ratio to frac. A light source will be subdivided
        until the width of each sample area divided by the distance to the
        illuminated point is below this ratio. This assures accuracy in regions
        close to large area sources at a slight computational expense. A value
        of zero turns source subdivision off, sending at most one shadow ray to
        each light source.
        """

        self.addRadianceNumber('dt', descriptiveName='direct thresholding',
                               numType=float, attributeName='directThreshold')
        self.directThreshold = directThreshold
        """
        -dt frac

        Set the direct threshold to frac. Shadow testing will stop when the
        potential contribution of at least the next and at most all remaining
        light source samples is less than this fraction of the accumulated value.
        The remaining light source contributions are approximated statistically.
        A value of zero means that all light source samples will be tested for
        shadow.
        """

        self.addRadianceNumber('dc', descriptiveName='direct certainty',
                               numType=float, attributeName='directCertainty')
        self.directCertainty = directCertainty
        """
        -dc frac

        Set the direct certainty to frac. A value of one guarantees that the
        absolute accuracy of the direct calculation will be equal to or better
        than that given in the -dt specification. A value of zero only insures
        that all shadow lines resulting in a contrast change greater than the
        -dt specification will be calculated.
        """

        self.addRadianceNumber('dr', descriptiveName='direct relays',
                               numType=float, attributeName='directSecRelays')
        self.directSecRelays = directSecRelays
        """
        -dr N

        Set the number of relays for secondary sources to N. A value of 0 means
        that secondary sources will be ignored. A value of 1 means that sources
        will be made into first generation secondary sources; a value of 2 means
        that first generation secondary sources will also be made into second
        generation secondary sources, and so on.
        """

        self.addRadianceNumber('dp', descriptiveName='direct presampling density',
                               numType=int, attributeName='directPresampDensity')
        self.directPresampDensity = directPresampDensity
        """
        -dp D

        Set the secondary source presampling density to D. This is the number of
        samples per steradian that will be used to determine ahead of time
        whether or not it is worth following shadow rays through all the
        reflections and/or transmissions associated with a secondary source path.
        A value of 0 means that the full secondary source path will always be
        tested for shadows if it is tested at all.
        """

        self.addRadianceNumber('st', descriptiveName='specular threshold', numType=float,
                               attributeName='specularThreshold')
        self.specularThreshold = specularThreshold
        """
        -st frac

        Set the specular sampling threshold to frac. This is the minimum
        fraction of reflection or transmission, under which no specular sampling
        is performed. A value of zero means that highlights will always be
        sampled by tracing reflected or transmitted rays. A value of one means
        that specular sampling is never used. Highlights from light sources
        will always be correct, but reflections from other surfaces will be
        approximated using an ambient value. A sampling threshold between zero
        and one offers a compromise between image accuracy and rendering time.
        """

        self.addRadianceNumber('lw', descriptiveName='limit weight', numType=float,
                               attributeName='limitWeight')
        self.limitWeight = limitWeight
        """
        -lw frac

        Limit the weight of each ray to a minimum of frac. During ray-tracing,
        a record is kept of the estimated contribution (weight) a ray would have
        in the image. If this weight is less than the specified minimum and the
        -lr setting (above) is positive, the ray is not traced. Otherwise,
        Russian roulette is used to continue rays with a probability equal to
        the ray weight divided by the given frac.
        """

        self.addRadianceNumber('lr', descriptiveName='limit reflections', numType=int,
                               attributeName='limitReflections')
        self.limitReflections = limitReflections
        """
        -lr N
        Limit reflections to a maximum of N, if N is a positive integer. If N
        is zero, then Russian roulette is used for ray termination, and the
        -lw setting (below) must be positive. If N is a negative integer, then
        this sets the upper limit of reflections past which Russian roulette
        will be used. In scenes with dielectrics and total internal reflection,
        a setting of 0 (no limit) may cause a stack overflow.
        """

        self.addRadianceNumber('ss', descriptiveName='specular sampling', numType=float,
                               attributeName='specularSampling')
        self.specularSampling = specularSampling
        """
        -ss samp

        Set the specular sampling to samp. For values less than 1, this is the
        degree to which the highlights are sampled for rough specular materials.
        A value greater than one causes multiple ray samples to be sent to reduce
        noise at a commmesurate cost. A value of zero means that no jittering
        will take place, and all reflections will appear sharp even when they
        should be diffuse. This may be desirable when used in combination with
        image sampling to obtain faster renderings.
        """


        self.addRadianceNumber('ps',descriptiveName='pixel sampling rate',numType=int,
                               attributeName='pixelSampling')
        self.pixelSampling = pixelSampling
        """
        -ps size

        Set the pixel sample spacing to the integer size. This specifies the
        sample spacing (in pixels) for adaptive subdivision on the image plane.
        """

        self.addRadianceNumber('pt',descriptiveName='pixel sampling tolerance',numType=float,
                               attributeName='pixelTolerance')
        self.pixelTolerance = pixelTolerance
        """
        -pt frac

        Set the pixel sample tolerance to frac. If two samples differ by more
        than this amount, a third sample is taken between them.
        """

        self.addRadianceNumber('pj',descriptiveName='anti-aliazing jitter',numType=float,
                               attributeName='pixelJitter')
        self.pixelJitter = pixelJitter
        """-pj frac

        Set the pixel sample jitter to frac. Distributed ray-tracing performs
        anti-aliasing by randomly sampling over pixels. A value of one will
        randomly distribute samples over full pixels. A value of zero samples
        pixel centers only. A value between zero and one is usually best for
        low-resolution images.
        """

        self.addRadianceNumber('pa',descriptiveName='pixel aspect ratio',numType=float,
                               attributeName='pixelAspectRatio')
        self.pixelAspectRatio=pixelAspectRatio
        """
        -pa rat

        Set the pixel aspect ratio (height over width) to rat. Either the x or
        the y resolution will be reduced so that the pixels have this ratio for
        the specified view. If rat is zero, then the x and y resolutions will
        adhere to the given maxima.
        """


        self.addRadianceNumber('pm',descriptiveName='pixel motion blur',numType=float,
                               attributeName='pixelMotionBlur')
        self.pixelMotionBlur=pixelMotionBlur
        """
        -pm frac

        Set the pixel motion blur to frac. In an animated sequence, the exact
        view will be blurred between the previous view and the next view as
        though a shutter were open this fraction of a frame time. (See the
        -S option regarding animated sequences.) The first view will be blurred
        according to the difference between the initial view set on the command
        line and the first view taken from the standard input. It is not
        advisable to use this option in combination with the pmblur(1) program,
        since one takes the place of the other. However, it may improve
        results with pmblur to use a very small fraction with the -pm option,
        to avoid the ghosting effect of too few time samples.
        """

        self.addRadianceNumber('pd',descriptiveName='pixel depth-of-field',numType=float,
                               attributeName='pixelDepthOfField')
        self.pixelDepthOfField=pixelDepthOfField
        """
        -pd dia

        Set the pixel depth-of-field aperture to a diameter of dia (in world
        coordinates). This will be used in conjunction with the view focal
        distance, indicated by the length of the view direction vector given
        in the -vd option. It is not advisable to use this option in combination
        with the pdfblur(1) program, since one takes the place of the other.
        However, it may improve results with pdfblur to use a very small
        fraction with the -pd option, to avoid the ghosting effect of too
        few samples.
        """

        self.addRadianceTuple('av',descriptiveName='ambient value',tupleSize=3,
                              attributeName='ambientValue',numType=float)
        self.ambientValue = ambientValue
        """
        -av red grn blu

        Set the ambient value to a radiance of red grn blu . This is the final
        value used in place of an indirect light calculation. If the number of
        ambient bounces is one or greater and the ambient value weight is non-zero ,
        this value may be modified by the computed indirect values to improve
        overall accuracy.
        """

        self.addRadianceNumber('aw',descriptiveName='ambient weight',numType=int,
                              attributeName='ambientWeight')
        self.ambientWeight = ambientWeight
        """
        -aw N

        Set the relative weight of the ambient value given with the -av option
        to N. As new indirect irradiances are computed, they will modify the
        default ambient value in a moving average, with the specified weight
        assigned to the initial value given on the command and all other weights
        set to 1. If a value of 0 is given with this option, then the initial
        ambient value is never modified. This is the safest value for scenes
        with large differences in indirect contributions, such as when both
        indoor and outdoor (daylight) areas are visible
        """

        self.addRadianceBoolFlag('dv',descriptiveName='light source visibility',
                                 attributeName='directVisibility')
        self.directVisibility=directVisibility
        """
        -dv

        Boolean switch for light source visibility. With this switch off,
        sources will be black when viewed directly although they will still
        participate in the direct calculation. This option may be desirable in
        conjunction with the -i option so that light sources do not appear in
        the output.
        """

        self.addRadianceBoolFlag('bv',descriptiveName='back face visibility',
                                 attributeName='backFaceVisibility')
        self.backFaceVisibility=backFaceVisibility
        """
         -bv

        Boolean switch for back face visibility. With this switch off, back
        faces of opaque objects will be invisible to all rays. This is dangerous
        unless the model was constructed such that all surface normals on opaque
        objects face outward. Although turning off back face visibility does not
        save much computation time under most circumstances, it may be useful
        as a tool for scene debugging, or for seeing through one-sided walls
        from the outside. This option has no effect on transparent or translucent
        materials.
        """

        self.addRadianceBoolFlag('u', descriptiveName='uncorrelated random sampling',
                                 attributeName='uncorRandSamp')
        self.uncorRandSamp = uncorRandSamp
        """
        -u

        Boolean switch to control uncorrelated random sampling. When "off", a
        low-discrepancy sequence is used, which reduces variance but can result
        in a brushed appearance in specular highlights. When "on", pure Monte
        Carlo sampling is used in all calculations.
        """

    @property
    def isImageBasedRadianceParameters(self):
        """Return True to indicate this object is a RadianceParameters."""
        return True

    @property
    def quality(self):
        """Get and set quality.

        An integer between 0-2 (0:low, 1: medium or 2: high quality)
        """
        return self.__quality

    @quality.setter
    def quality(self, value):
        if value is None:
            self.__quality = None

            # add all numeric parameters
            for name, data in rpict_number_parameters.iteritems():
                self.addRadianceNumber(data['name'], data['dscrip'], numType=data['type'],
                                       attributeName=name)

            # add boolean parameters
            for name, data in rpict_boolean_parameters.iteritems():
                self.addRadianceBoolFlag(data['name'], data['dscrip'],
                                         attributeName=name)
        else:
            assert (0 <= int(value) <= 2), \
                "Quality can only be 0:low, 1: medium or 2: high quality"

            self.__quality = int(value)
            """An integer between 0-2 (0:low, 1: medium or 2: high quality)"""

            # add all numeric parameters
            for name, data in rpict_number_parameters.iteritems():
                self.addRadianceNumber(data['name'], data['dscrip'], numType=data['type'],
                                       attributeName=name)
                setattr(self, name, data['values'][self.quality])

            # add boolean parameters
            for name, data in rpict_boolean_parameters.iteritems():
                self.addRadianceBoolFlag(data['name'], data['dscrip'], attributeName=name)
                setattr(self, name, data['values'][self.quality])

    def getParameterDefaultValueBasedOnQuality(self, parameter):
        """Get parameter value based on quality.

        You can change this value by using self.parameter = value (e.g. self.ab=5)

        Args:
            parameter: Radiance parameter as an string (e.g "ab")

        Usage:

            rp = LowQuality()
            print rp.getParameterValue("ab")
            >> 2
        """
        if not self.quality:
            print "Quality is not set! use self.quality to set the value."
            return None

        __key = str(parameter)

        assert __key in self.keys, \
            "%s is not a valid radiance parameter" % str(parameter)

        return rpict_boolean_parameters[__key]["values"][self.quality]

#@mostaphaRoudsari, added Image to the end of LowQuality, MediumQuality etc so that there
# is no conflict with Gridbased parameters of similar names.

class LowQualityImage(ImageBasedParameters):
    """Radiance parmaters for a quick analysis."""

    def __init__(self):
        """Create low quality radiance parameters for quick studies."""
        ImageBasedParameters.__init__(self, quality=0)


class MediumQualityImage(ImageBasedParameters):
    """Medium quality Radiance parmaters."""

    def __init__(self):
        """Create medium quality radiance parameters."""
        ImageBasedParameters.__init__(self, quality=1)


class HighQualityImage(ImageBasedParameters):
    """High quality radiance parameters."""

    def __init__(self):
        """Create high quality radiance parameters."""
        ImageBasedParameters.__init__(self, quality=2)
