from inv_db import add_product, update_product, delete_product, fetch_products
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Management System", page_icon="📦", layout="wide")

st.markdown("<h1 style='text-align: center;'>📦 Inventory Management System</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Page background: soft black */
    .stApp {
        background: linear-gradient(120deg, #eceff1, #f8f9fa);
        background-attachment: fixed;
    }

    /* Main title */
    .main-title {
        color: #1e90ff;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Column / section titles */
    .section-header {
        color: #1e90ff;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    /* Columns / cards */
    .stCard, .stContainer {
        background: silver;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        color: white;  /* Ensure text is readable */
    }

    /* Buttons with silver background and black text/border */
        div.stButton > button:first-child {
        background: silver;           /* Button background */
        color: black;                      /* Button text color */
        border: 2px solid black;         /* Button border */
        border-radius: 8px;           /* Rounded corners */
        padding: 0.5em 1.2em;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s;
}

        div.stButton > button:first-child:hover {
        transform: scale(1.05);      /* Slight scale on hover */
}

        div.stButton > button:first-child:hover {
                transform: scale(1.05);
    }

    /* Input fields */
    input[type="text"], input[type="number"] {
        background: white;
        color: black;
        border: 2px solid  #111111; 
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        outline: none;
        transition: transform 0.2s;
    }

    input[type="text"]:hover, input[type="number"]:hover {
        transform: scale(1.03);
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100vw;
        background-color: rgba(255,255,255,0.9);
        padding: 12px 0;
        text-align: center;
        border-top: 1px solid #ccc;
        font-size: 18px;
        font-weight: bold;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

# 3 columns creation
col1, col2, col3 = st.columns(3)

# product adding section
with col1:
    st.subheader("Add Product")
    name = st.text_input("Product Name", key="add_name")
    quantity = st.number_input("Quantity", min_value=0, key="add_quantity")
    price = st.number_input("Price (₹)", min_value=0.0, format="%.2f", key="add_price")
    
    if st.button("Add Product"):
        if name:
            msg = add_product(name, quantity, price)
            st.success(msg)
        else:
            st.error("Please enter a product name")

# product updating section
with col2:
    st.subheader("Update Product")
    update_id = st.number_input("Product ID", min_value=0, step=1, key="update_id")
    update_quantity = st.number_input("New Quantity", min_value=0, key="update_quantity")
    update_price = st.number_input("New Price (₹)", min_value=0.0, format="%.2f", key="update_price")
    
    if st.button("Update Product"):
        if update_id > 0:
            msg = update_product(update_id, update_quantity, update_price)
            st.success(msg)
        else:
            st.error("Please enter a valid Product ID")

# product deleting section
with col3:
    st.subheader("Delete Product")
    delete_id = st.number_input("Product ID", min_value=0, step=1, key="delete_id")
    
    if st.button("Delete Product"):
        if delete_id > 0:
            msg = delete_product(delete_id)
            st.success(msg)
        else:
            st.error("Please enter a valid Product ID")

# products showing section
total_value = 0  

st.markdown("---")
if st.button("Show all products"):
    products = fetch_products()
    if products:
        df = pd.DataFrame(products, columns=["Product ID", "Product Name", "Quantity", "Price"])
        df["Price"] = df["Price"].apply(lambda x: f"₹{x:,.2f}")
        st.dataframe(df, height=300, use_container_width=True, hide_index=True)

        total_value = sum([row[2]*row[3] for row in products])
    else:
        st.info("No products found")
        total_value = 0

# footer section
st.markdown(f"""
    <div style="
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px;
        text-align: center;
        border-top: 2px solid #ccc;
        font-size: 18px;
        font-weight: bold;
    ">
        Total Inventory Value: ₹{total_value:,.2f}
    </div>
    <div style="height:50px;"></div> <!-- spacer -->
""", unsafe_allow_html=True)
