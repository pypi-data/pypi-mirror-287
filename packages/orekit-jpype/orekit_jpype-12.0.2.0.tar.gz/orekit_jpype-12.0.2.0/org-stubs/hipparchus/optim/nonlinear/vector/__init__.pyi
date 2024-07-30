
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.optim.nonlinear.vector.leastsquares
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.vector")``.

    leastsquares: org.hipparchus.optim.nonlinear.vector.leastsquares.__module_protocol__
