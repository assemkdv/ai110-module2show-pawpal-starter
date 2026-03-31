from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# create owner (temporary)
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Assem")

owner = st.session_state.owner

st.header("Add a Pet")

pet_name = st.text_input("Pet Name")
pet_type = st.text_input("Pet Type")
pet_age = st.number_input("Pet Age", min_value=0)

if st.button("Add Pet"):
    if pet_name and pet_type:
        new_pet = Pet(pet_name, pet_type, pet_age)
        owner.add_pet(new_pet)
        st.success(f"{pet_name} added successfully!")
    else:
        st.error("Please enter pet name and type")
    
st.header("Your Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"🐾 {pet.name} ({pet.type}, {pet.age} years old)")
else:
    st.write("No pets added yet.")

st.header("Add Task")

if owner.pets:
    pet_names = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Select Pet", pet_names)

    task_desc = st.text_input("Task Description")

    if st.button("Add Task"):
        for pet in owner.pets:
            if pet.name == selected_pet_name:
                task = Task(
                    description=task_desc,
                    scheduled_time=datetime.now(),
                    priority=1,
                    frequency="daily"
                )
                pet.add_task(task)
                st.success("Task added!")
else:
    st.warning("Add a pet first before adding tasks.")

st.header("Today's Schedule")

scheduler = Scheduler(owner)

if st.button("Generate Schedule"):
    tasks_today = scheduler.generate_daily_plan()

    if tasks_today:
        for task in tasks_today:
            time_str = task.scheduled_time.strftime("%I:%M %p")
            st.write(f"- {task.description} at {time_str}")
    else:
        st.write("No tasks scheduled for today.")



