import streamlit as st

# Page setup (must be before other Streamlit calls)
st.set_page_config(page_title="ARC | DocChain", page_icon="📦", layout="centered")

# Page styling
st.markdown(
    """
<style>
body {
background-color: black;
color: #00BFFF;
}
h1, h2, h3, label, p {
color: #00BFFF !important;
}
.stButton>button {
background-color: #00BFFF;
color: white;
border: none;
border-radius: 5px;
height: 2.5em;
width: 10em;
}
</style>
""",
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("ARC | DocChain")
st.subheader("Smart AI + Blockchain Export Document Manager")
st.markdown("---")

# Step 1: Company Information
st.header("Step 1: Company Information")
company_name = st.text_input("Company Name")
email = st.text_input("Email Address", placeholder="you@example.com")
phone = st.text_input("Phone Number", placeholder="+1-555-555-5555")
reg_no = st.text_input("Company Registration Number")
st.markdown("---")

# Step 2: Select Trade Region
st.header("Step 2: Select Trade Region")
region = st.selectbox(
    "Choose your trade region",
    ["Select", "Asia", "Europe", "Middle East", "North America", "South America", "Africa"],
)

if region != "Select":
    st.info(
        f"🧠 AI Recommendation: For {region} exports, required documents typically include: "
        "Invoice, Packing List, Bill of Lading, Certificate of Origin, and Country-Specific Permits."
    )
    st.markdown("---")

# Step 3: Upload Trade Documents
st.header("Step 3: Upload Trade Documents")
uploaded_files = st.file_uploader(
    "Upload your trade documents (PDF, DOCX, etc.)", accept_multiple_files=True, type=["pdf", "docx", "doc", "txt"]
)

if uploaded_files:
    for file in uploaded_files:
        st.success(f"✅ {file.name} uploaded successfully!")
    st.markdown("---")

# Step 4: AI + Blockchain Verification Simulation
st.header("Step 4: AI & Blockchain Verification")
if st.button("Run Verification"):
    st.info("⚙️ AI is analyzing documents for compliance and accuracy...")
    # Placeholder for actual AI/verification logic
    st.success("✅ Documents verified successfully and Blockchain-stamped for traceability!")
    st.markdown("---")

# Footer
st.caption("🔗 Powered by ARC | DocChain — Secure, Smart & Seamless Trade.")
