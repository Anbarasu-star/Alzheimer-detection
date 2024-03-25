import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config("MIND HEAL Detection",page_icon="🧠",layout='wide',initial_sidebar_state='collapsed')
video_html = """
<style>
[data-testid="stHeader"]{
   background-color: rgba(0,0,0,0);
}
"""

st.markdown(video_html, unsafe_allow_html=True)


@st.cache_resource(show_spinner="loading...")
def load_lottie():
    r = requests.get("https://assets7.lottiefiles.com/packages/lf20_wzq5hrhg.json")
    if r.status_code != 200:
        return None
    return r.json()
with st.sidebar:
    lottie_json = load_lottie()
    st_lottie = st_lottie(lottie_json,speed=2,loop=True,quality="high",height=300, width=300)

st.title("Welcome to MIND HEAL! 🔍")

st.info("Dementia prediction 🧠 By using advanced technology to analyze MRI brain images, our groundbreaking solution accurately predicts the severity of the disease. It categorizes Alzheimer's into different levels: mild, moderate, very mild, and non-dementia. With an impressive accuracy rate , our model paves the way for early intervention and personalize care..")

st.subheader("What is Dementia ?")

st.write(""" 
Dementia is a term for several diseases that affect memory, thinking, and the ability to perform daily activities. The illness gets worse over time. It mainly affects older people but not all people will get it as they age. Dementia is a syndrome that can be caused by a number of diseases which over time destroy nerve cells and damage the brain, typically leading to deterioration in cognitive function (i.e. the ability to process thought) beyond what might be expected from the usual consequences of biological ageing According to papers from Lancet neurology, even the old theory such as neural inflations, which was disregarded as the cause compared to tau-protein, beta-amyloids, and genetic factors. The World Health Organization Trusted Source says that 47.5 million people around the world are living with dementia. The National Institutes of Health estimate that more than 5 million people in the United States have Alzheimer’s disease. Although younger people can and do get Alzheimer's, the symptoms generally begin after age 60. There are degrees of severity in Alzheimer.

Very mildly demented: This is the stage where patient starts to forget where they put their stuff, other people's names recently, etc. It is hard to detect through cognitive ability test.

Mildly demented: This is the stage where patients don't remember the words, can't find their way to the destination, loss of focus and work-abilities. This is also the stage where patients even forget that they are losing memory. From this stage, with cognitive testing, it can be found.

Moderately demented: Starts to forget the recent activities, important old histories, have hard time calculating the budget, hard to go outside alone, and loss of empathy.
There are 3 more stages in the moderately dementia, which in the terminal stage, the patient can't move on their own, while they lose the ability to speak. Knowing these stages are important because the faster the stage the patient is at, the treatment will have higher effect in terms of slowing the process. If the dementia is found during the moderately demented stage, it is known that the patient will pass away in 3 years. Thus, having an AI that detects alzheimer dementia in the early stage can allow longer life expectancy from the patient as well as higher life quality overall from the slowdown of dementia. As Alzheimer can not only be found with cognitive ability testing, but also through MRI or CT by looking at the ventricles of the brain and cortical atrophy, the theoretical foundation on this project is solid. Doctors find the patient with Alzheimer's have a brain that have enlarged ventricles (that lies in the center of the brain) as well as thinner cortical grey area of the brain.""")