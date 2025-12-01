import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

st.title("📊 Statistical Distribution Fitting Tool")

tab1, tab2 = st.sidebar.tabs(["Data Input", "Distribution Selection"])

with tab1:
    st.header("Data Input")
    
    data_text = st.text_area(
        "Enter data (comma or space separated):", 
        height=120,
        placeholder="1.2, 3.4, 2.2, 5.1, ..."
    )
    
    data = None
    
    def extract(txt):
        try:
            txt = txt.replace("\n", " ")
            txt = txt.replace(",", "")
            return np.array([float(x) for x in txt.split() if x.strip() != ""])
        except:
            return None
    
    file = st.file_uploader("Or upload a csv file", type=["csv"])
    
    if file:
        df = pd.read_csv(file)
        col = st.selectbox("Select column from CSV (if you named you columns):", df.columns)
        data = df[col].dropna().values

    else:
        data = extract(data_text)
        
    if data is None or len(data) < 2:
        st.warning("Please enter at least 2 valid numbers or upload a CSV to proceed.")
        st.stop()
        
with tab2:
    st.header("📦 Distribution Selection")
    st.write("Choose a distribution to fit:")
    
    dist_names = {
        "Normal": stats.norm,
        "Gamma": stats.gamma,
        "Weibull": stats.weibull_min,
        "Exponential": stats.expon,
        "Beta": stats.beta,
        "Lognormal": stats.lognorm,
        "Chi-square": stats.chi2,
        "Laplace": stats.laplace,
        "Cauchy": stats.cauchy,
        "Uniform": stats.uniform,
    }
    
    dist_choice = st.selectbox("Distribution", list(dist_names.keys()))

    st.write(f"You selected: {dist_choice}")
    
    try:
        params = dist_names[dist_choice].fit(data)
        param_df = pd.DataFrame({
            "Parameter": [f"param_{i+1}" for i in range(len(params))],
            "Value": [p for p in params]
            })
        st.subheader("📐 Fitted Parameters")
        st.table(param_df)
    except Exception as e:
        st.error(f"Fitting failed: {e}")

with st.expander("🔧 Manual Parameter Adjustment", expanded=False):
    st.write("Use these sliders to manually override distribution parameters.")

    sliders = []
    new_params = []

    for i, p in enumerate(params):
        
        new_val = st.slider(
            f"Parameter {i+1} (initial: {p:.3f})",
            min_value= float(p * 0.1 - 10),
            max_value= float(p * 2 + 10),
            value= float(p),
            step=0.01
        )
        
        new_params.append(new_val)

    params = tuple(new_params)
    
if data is not None and len(data) > 1:
    x = np.linspace(min(data), max(data), 500)
    pdf_vals = dist_names[dist_choice].pdf(x, *params)

    hist_y, hist_x = np.histogram(data, bins=20, density=True)
    hist_centers = (hist_x[:-1] + hist_x[1:]) / 2

    pdf_interp = np.interp(hist_centers, x, pdf_vals)

    mae = np.mean(np.abs(hist_y - pdf_interp))
    max_error = np.max(np.abs(hist_y - pdf_interp))

    st.markdown("---")
    st.header("📈 Data & Fitted Distribution")

    plt.style.use("ggplot")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        data, bins=20, density=True, alpha=0.6,
        color="steelblue", edgecolor="black", linewidth=1.2,
        label="Data Histogram"
    )

    ax.plot(
        x, pdf_vals, color="darkred", lw=3, linestyle="-",
        label=f"{dist_choice} Fit"
    )

    ax.set_xlabel("Value", fontsize=14, fontweight="bold")
    ax.set_ylabel("Density", fontsize=14, fontweight="bold")
    ax.set_title(f"Distribution Fit: {dist_choice}", fontsize=16, fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend(frameon=True, fontsize=12)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    st.pyplot(fig)

    st.markdown("---")
    st.subheader("📊 Fit Quality Metrics")
    st.write(f"**Mean Absolute Error (MAE):** {mae:.5f}")
    st.write(f"**Maximum Error:** {max_error:.5f}")
else:
    st.info("No valid data yet — please enter numbers or upload a CSV.")