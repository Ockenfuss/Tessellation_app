import streamlit as st
import matplotlib.pyplot as plt
import math
import imageio
import numpy as np
from crazybin import imshow

def main():
    # Create three columns
    col1, col2, col3 = st.columns([2,1.4,2])

    # Display an image in each column
    col1.image('examples/images/grande_jatte_seurat.jpg', use_column_width=True)
    col3.image('examples/images/great_wave.jpg', use_column_width=True)
    col2.image('examples/images/hex_rhomb.jpg', use_column_width=True)

    st.title("Image Tessellation")
    st.write("This app allows you to transform your images into a parquet of small tiles.")
    st.write("Just upload an image and select the type of tile you want together with the resolution.")
    st.write("The app is powered by [crazybin](https://github.com/Ockenfuss/crazybin), a python module to visualize images and histograms as tessellations.")

    tile_descriptions = {
            "Regular hexagon": "hex",
            "Composition of a regular hexagon, triangles and squares": "hex_rhomb",
            "Composition of three lizard shaped tiles inspired by M.C. Escher": "reptile",
            "Composition of four frog shaped tiles inspired by M.C. Escher.": "frog", 
            "Irregular P3 penrose tiling, consisting of two rhombs with different angles.": "pen_rhomb",
        }
    tile_types={"hex": "regular", "hex_rhomb": "regular", "reptile": "regular", "frog": "regular", "pen_rhomb": "irregular"} 
    
    file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    selected_description = st.selectbox("Choose a tile type", list(tile_descriptions.keys()))
    tile_key=tile_descriptions[selected_description]
    slidermax=10
    resolution = st.slider("Choose the resolution", min_value=1, max_value=slidermax, value=5)

    if file is not None:
        image = imageio.imread(file)
        if image.dtype != np.float32:
                image = image / 255.0  # Normalize to [0, 1] range
        st.subheader("Original Image:")
        st.image(image, use_column_width=True)

        if tile_types[tile_key]=="regular":
            #go exponentially from 1 to 100
            resolution=math.ceil(100**((resolution-1)/(slidermax-1)))


        st.subheader("Tessellated image:")
        print(resolution)
        print(tile_types[tile_key])
        fig, ax = plt.subplots()
        imshow(image, tile=tile_key, ax=ax, gridsize=resolution)
        ax.axis('off')
        st.pyplot(fig)

if __name__ == "__main__":
    main()