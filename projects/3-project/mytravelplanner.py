from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.set_page_config(page_title="My Travel Planner", page_icon="🌏")
st.title("🌏 My Travel Planner")
st.write(
    "Plan your next trip with the help of AI! Enter your destination and travel dates, and let the AI suggest an itinerary for you."
)
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

            st.subheader("🌴 Tourist Places")
            places = places_chain.invoke({"location": location})
            st.write(places)

            st.subheader("🏨 Recommended Hotels")
            hotels = hotels_chain.invoke({"location": location})
            st.write(hotels)

            st.subheader("📅 Itinerary")
            itinerary = itinerary_chain.invoke({"places": places})
            st.write(itinerary)

            st.subheader("💰 Budget Estimate")
            budget = budget_chain.invoke({"itinerary": itinerary})
            st.write(budget)

            st.subheader("💡 Travel Tips")
            tips = tips_chain.invoke({"location": location})
            st.write(tips)

            st.success("✅ Your trip has been planned! Enjoy your travels!")
