import google.generativeai as genai
import streamlit as st
import time

# Set up the Gemini API with your API key
genai.configure(api_key="AIzaSyAvKRVv-AYQ1z8F4t83F_OKO9h4UjC42PA")  # Replace with your actual API key

# Define a function to get recommendations using the Gemini API
def get_gemini_recommendations(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use the appropriate Gemini model
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI Components
st.set_page_config(page_title="Travel Spot Generator", page_icon=":earth_americas:", layout="wide")

# Add a header with animation
st.title("🌍 Travel Spot Generator")
st.markdown("""
    ## Enter your preferences to generate a personalized travel itinerary.
    Discover the best activities, transport, food, and lodging based on your travel needs!
""")

# Add a little animation using streamlit's progress bar
st.markdown("""
    <style>
    .css-1hdg7cl {
        text-align: center;
        font-size: 24px;
        color: #1e90ff;
    }
    </style>
""", unsafe_allow_html=True)

# Add a form with smoother transitions
with st.form(key='itinerary_form'):
    experience_type = st.selectbox("🔍 Experience Type", ["Adventure", "Cultural", "Relaxation", "Nature"])
    location = st.text_input("📍 Location")
    travel_period = st.text_input("📅 Travel Period (e.g., 3 days, 2 weeks)")
    group_type = st.selectbox("👨‍👩‍👧‍👦 Group Type", ["Solo", "Couple", "Family", "Group of Friends"])
    budget = st.selectbox("💸 Budget", ["Low", "Medium", "High"])
    special_interests = st.text_area("🎯 Special Interests (optional)", help="Share your unique preferences!")
    language = st.text_input("🌐 Preferred Language (optional)")

    submit_button = st.form_submit_button("Explore")

# Show animation and delay when generating recommendations
if submit_button:
    # Show loading spinner
    with st.spinner("Generating your travel itinerary... This may take a moment! 🕰️"):
        time.sleep(2)  # Simulate the waiting time while generating

    # Extract input values
    special_interests = special_interests if special_interests else 'general preferences'
    
    # Create the input query for Gemini model
    prompt = f"""Please provide a detailed travel itinerary in {language} for a {group_type.lower()} traveler interested in a {budget.lower()} {experience_type.lower()} exploration. The itinerary should focus on the following aspects:
    
- **Location**: Include recommendations for areas around {location}.
- **Travel Period**: {travel_period}.
- **Special Interests**: Highlight attractions relevant to {special_interests}.

**Itinerary Format**:
- **Day-by-Day Breakdown**: Clearly label each day and list activities or places to visit in bullet points.
- **Historical/Relevant Attractions**: Prioritize key landmarks or interests (e.g., forts, museums, or specific local spots).
- **Transportation**: Suggest budget-friendly transportation options and provide travel tips.
- **Accommodation**: Recommend affordable guesthouses, hostels, or budget hotels nearby.
- **Food and Dining**: Mention any local food spots or must-try delicacies.
- **Important Notes**: Include travel tips like safety, local norms, and negotiating with drivers.

The response should follow this structured format:

**Day X: [Day Title]**
- Activities:
  - [Activity 1]
  - [Activity 2]
- Transportation: [Suggestion]
- Accommodation: [Suggestion]
- Dining: [Suggestion]

Ensure the content is practical, concise, and helpful for {group_type.lower()} travelers with a {budget.lower()} budget."""

    # Get the response from the Gemini model
    recommendations = get_gemini_recommendations(prompt)
    
    # Show success animation after processing
    st.balloons()

    # Display the recommendations with a header
    st.subheader("🎉 Generated Tourist spots Recommendations:")
    st.write(recommendations)

    # Add a button to reset the form (Optional)
    if st.button('🔄 Reset Form'):
        st.experimental_rerun()


