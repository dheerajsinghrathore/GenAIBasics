import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()
UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")
st.set_page_config(page_title="My Travel Planner", page_icon="🌏")
st.title("🌏 My Travel Planner")
st.write(
    "Plan your next trip with the help of AI! Enter your destination and travel dates, and let the AI suggest an itinerary for you."
)


def get_travel_image(location):
    url = f"https://api.unsplash.com/search/photos?query={location}&client_id={UNSPLASH_API_KEY}&per_page=1"
    try:
        response = requests.get(url)
        data = response.json()
        if data["results"]:
            return data["results"][0]["urls"]["regular"]
    except Exception as e:
        st.error(f"Error fetching travel image for {location}: {e}")
    return None


location = st.text_input("Enter Location: ")
if st.button("Plan My Trip"):
    if location.strip() == "":
        st.warning("Please enter a location to plan your trip.")
    else:
        with st.spinner("Planning your trip..."):
            llm = ChatOpenAI(model="gpt-3.5-turbo")

            places_prompt = ChatPromptTemplate.from_template(
                "Create a 5-day itinerary for a trip to {location}.Include activities, restaurants, and sightseeing spots."
            )
            places_chain = places_prompt | llm | StrOutputParser()

            hotels_prompt = ChatPromptTemplate.from_template(
                "Find 3 recommended hotels in {location} with ratings above 4 stars."
            )
            hotels_chain = hotels_prompt | llm | StrOutputParser()

            itinerary_prompt = ChatPromptTemplate.from_template(
                "Create a 5-day itinerary for a trip to {places}.Include activities, restaurants, and sightseeing spots."
            )
            itinerary_chain = itinerary_prompt | llm | StrOutputParser()

            budget_prompt = ChatPromptTemplate.from_template(
                "Estimate a daily budget for a trip to {itinerary}, including accommodation, food, and activities."
            )
            budget_chain = budget_prompt | llm | StrOutputParser()

            tips_prompt = ChatPromptTemplate.from_template(
                "Provide travel tips for a trip to {location}."
            )
            tips_chain = tips_prompt | llm | StrOutputParser()

            places = places_chain.invoke({"location": location})
            hotels = hotels_chain.invoke({"location": location})
            itinerary = itinerary_chain.invoke({"places": places})
            budget = budget_chain.invoke({"itinerary": itinerary})
            tips = tips_chain.invoke({"location": location})

            st.subheader("🌴 Tourist Places")
            cols = st.columns(3)
            places_list = places.split("\n")[:5]  # Get the first 5 places
            for i, place in enumerate(places_list):
                with cols[i % 3]:
                    st.write(place)
                    image_url = get_travel_image(place)
                    if image_url:
                        st.image(image_url, use_column_width=True)
                    else:
                        st.warning(f"No image found for {place}.")
                    st.markdown(f"---{place}---")
            st.write(places)

            st.subheader("🏨 Recommended Hotels")
            st.write(hotels)

            st.subheader("📅 Itinerary")
            st.write(itinerary)

            st.subheader("💰 Budget Estimate")
            st.write(budget)

            st.subheader("💡 Travel Tips")
            st.write(tips)

            st.success("✅ Your trip has been planned! Enjoy your travels!")
