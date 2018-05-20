"""This module is intended to provide easy set up for an aguaclara playground
/environment.

It imports all commonly used aide packages with one line, ensures Python is
run in the correct virtual environment, sets sig figs correctly and provides
any additional environment massaging to get to designing as quickly as
possible. This should NOT be used by other modules within aide_design as it
results in unnecessary imports.

Usage:

    * Import all into your global namespace with: `from aguaclara_research.play import *`
    * setup_aguaclara() should run during import.

Now you should be able to execute:
    *`np.array([1,2,3,4])
And your numbers should be limited to four significant figures  when printed.

"""

# AIDE imports
# pandas, numpy, matplotlib, math, and AIDE specific packages (like constants)
from aide_design.play import *
import aguaclara_research.ProCoDA_Parser as pro
import aguaclara_research.Environmental_Processes_Analysis as epa
import aguaclara_research.floc_model as floc_mod

def setup_aguaclara():
    """
    This is the public function that should be called to completely setup the aide environment
    in a jupyter notebook.
    :return:
    """
    matplotlib.style.use('ggplot')
    set_sig_fig()
    #ensure_in_a_virtual_environment()
        # Don't want to scare the kiddos with virtual environments yet! TODO.

def set_sig_fig(n=4):
    """Set the default number of significant figures used to print pint, pandas and numpy values
    quantities. Defaults to 4.

    Args:
        n: number of significant figures to display

    Example:
        import aguaclara_research
        from aide_design.units import unit_registry as u
        h=2.5532532522352543*u.m
        e = 25532532522352543*u.m
        print('h before sigfig adjustment: ',h)
        print('e before sigfig adjustment: ',e)
        aide_design.units.set_sig_fig(10)
        print('h after sigfig adjustment: ',h)
        print('e after sigfig adjustment: ',e)

        h before sigfig adjustment:  2.553 meter
        e before sigfig adjustment:  2.553e+16 meter
        h after sigfig adjustment:  2.553253252 meter
        e after sigfig adjustment:  2.553253252e+16 meter
    """
    assert isinstance(n, int), "Input must be an integer"
    u.default_format = '.' + str(n) + 'g'
    pd.options.display.float_format = ('{:,.' + str(n) + '}').format


def ensure_in_a_virtual_environment():
    """
    Warn users if not in a virtual environment
    """
    import sys
    # way to test for virtual environment: https://stackoverflow.com/a/1883251/5136799
    if hasattr(sys, 'real_prefix'):
        raise UserWarning("aide_design should always be run in a virtual environment to ensure"
                          "that all dependencies are correctly installed. Please refer to the"
                          "readme for virtual environment setup instructions.")

# Run when imported
setup_aguaclara()
