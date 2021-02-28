import streamlit as st
from pycbc.waveform import get_td_waveform
import pylab


st.set_page_config(page_icon="〰", page_title="GW Waveform Generator")

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #272626;

    }
}
</style>
    """, unsafe_allow_html=True)

st.title('GW Waveform Generator ∿')

st.markdown(""" ------------------------------------------------------------------------- """)

st.subheader(""" Check left panel to change input parameters """)

st.markdown(""" ------------------------------------------------------------------------- """)

st.markdown("""∿ Visit the GWOSC website to try out other GW data analysis on your own: https://www.gw-openscience.org/tutorials/ """)
st.markdown("""∿ The implementation of this model can be studied in detail over here: https://arxiv.org/pdf/1611.03703.pdf""")
st.markdown("""∿ You can learn more about PyCBC and Time Domain waveforms over here: http://pycbc.org/pycbc/latest/html/waveform.html""")



distancev = []

approx = st.sidebar.selectbox( 'Select the approximant:',
('SEOBNRv4_opt', 'IMRPhenomA', 'IMRPhenomB', 'IMRPhenomC', 'IMRPhenomD', 'IMRPhenomD_NRTidalv2'))

massv1 = st.sidebar.number_input('Mass 1 (In Solar mass)', min_value=5, max_value=1000)
massv2 = st.sidebar.number_input('Mass 2 (In Solar mass)', min_value=5, max_value=1000)

distancev1 = st.sidebar.number_input('Distance 1 (Mpc)', 100)
distancev2 = st.sidebar.number_input('Distance 2 (Mpc)', 500)
distancev3 = st.sidebar.number_input('Distance 3 (Mpc)', 1000)

distancev.append(distancev1)
distancev.append(distancev2)
distancev.append(distancev3)

st.markdown("""
→ Choose the time between samples t (s). Using a 4096-second data.""")

st.markdown("""→ You can also change the value for starting gravitaional-wave frequency.
""")

st.markdown(""" ------------------------------------------------------------------------- """)

t = st.sidebar.number_input('Time between samples (s)', 1)
deltat = t/4096

f_low = st.sidebar.number_input('Lower GW frequency (Hz). Max value (169)', 30)

for d in distancev:
    hp, hc = get_td_waveform(approximant= approx,
                         mass1=massv1,
                         mass2=massv2,
                         delta_t=deltat,
                         f_lower=f_low,
                         distance=d)

    pylab.plot(hp.sample_times, hp, label='$Distance=%sMpc$' % d)

st.set_option('deprecation.showPyplotGlobalUse', False)

pylab.legend()
pylab.grid()
pylab.xlabel('Time (s)')
pylab.show()
st.pyplot()



st.markdown("""Kindly request changes or additions to the web app through the repository found here: https://github.com/darthnair/gwwaveform""")
