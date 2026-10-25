## Import Streamlit
import streamlit as st


## Page heading
st.title("🌾 Farming Education")

## Introduction
st.write("Learn about different climate-resilient farming techniques.")
technique_1 = st.container(border=True)
technique_2 = st.container(border=True)
technique_3 = st.container(border=True)
technique_4 = st.container(border=True)
technique_5 = st.container(border=True)
technique_6 = st.container(border=True)
technique_7 = st.container(border=True)
technique_8 = st.container(border=True)
technique_9 = st.container(border=True)
technique_10 = st.container(border=True)

## technique 1
with technique_1:
    st.header("Drip Irrigation")
    st.write("In drip irrigation, water is run through pipes (with holes in them) either buried or lying slightly above the ground next to the crops. Water slowly drips onto the crop roots and stems.  ")
    with st.expander("Advantages"):
        st.write('''
**Saves water**: Water is delivered directly to the plant's root zone, so less is lost through evaporation, runoff, and wind.\n
**High efficiency**: Drip systems can be about 90-95% efficient because they apply water only where plants need it.\n
**Better crop growth and yields**: Plants receive a steady, controlled supply of moisture, which can improve growth and yields, especially in dry or sandy soils.\n
**Less weed growth**: Because only a small area of soil is wet, fewer weed seeds germinate.\n
**Fewer leaf diseases**: The plant leaves stay dry, reducing diseases that spread when foliage remains wet.\n
**Can reduce labour**: Once installed, the system can be operated by opening a valve or automated, reducing the need for manual watering.\n
**Works on many soils and slopes**: Drip irrigation can be used on different soil types and sloped land where flood irrigation may be difficult.
''')

## technique 2
with technique_2:
    st.header("Rainwater Harvesting")
    st.write("something abour rain idk")

## technique 3
with technique_3:
    st.header("Mulching")
    st.write("i think that's dirt mebbe")

## technique 4
with technique_4:
    st.header("Cover Cropping")
    st.write("you know when you give plants those tiny thingies to keep them safe from the rain? yeah, me neither")

## technique 5
with technique_5:
    st.header("Crop Rotation")
    st.write("Crop rotation is the planned practice of growing different types of crops on the same piece of land in a planned sequence over several seasons, rather than planting the same crop every year. For example, a farmer may grow legumes such as beans one season, then maize or another crop the next season. This helps maintain soil fertility and reduces pests and diseases. ")
    with st.expander("Advantages"):
            st.write('''
    **Improves soil fertility**: Different crops use nutrients in different ways, so rotation helps balance nutrient use and recycle nutrients in the soil. \n
**Adds nitrogen to the soil**: Legumes such as beans, peas, and clover can fix nitrogen through a relationship with soil bacteria, providing nitrogen for the crops that follow. \n
**Reduces pests and diseases**: Changing crops breaks the life cycles of pests, weeds, and diseases that depend on one particular crop, reducing the chance that they build up in the soil.\n
**Reduces the need for chemicals**: Because pests and diseases are less able to build up, farmers may need less pesticide and fertilizer. \n
**Improves soil structure and health**: Rotating deep-rooted and shallow-rooted crops creates different root channels, improves water movement, and supports a wider range of beneficial soil organisms. \n
**Reduces soil erosion**: Crop rotation can improve soil cover and organic matter, helping reduce sheet, rill, and wind erosion. 
    ''')

## technique 6
with technique_6:
    st.header("Agro-Forestry and Windbreakers")
    st.write("I'm pretty sure that's agriculture and forest something. Pretty sure windbreakers are the stuff that breaks the wind.")

## technique 7
with technique_7:
    st.header("Hurricane-Resistant Greenhouses")
    st.write("I- does that mean what I think it means? how do you even-?????????")

## technique 8
with technique_8:
    st.header("Hydroponics/Aquaponics")
    st.write("...hydro is water? And I think aqua is also water? ponics is.... idk bro")

## technique 9
with technique_9:
    st.header("Solar-Powered Irrigation Systems")
    st.write("How do you use the sun to keep your plants wet? idk, ask the experts. I'm just the design guy.")

## technique 10
with technique_10:
    st.header("Contour Cropping")
    st.write("Contour cropping, also called contour farming or contour ploughing, is a soil-conservation method in which crops are planted in rows that follow the natural curves or contours of a slope, rather than straight up and down the hill. These rows act like small barriers that slow rainwater runoff, allowing more water to soak into the soil and reducing the amount of soil washed away.")
    with st.expander("Advantages"):
        st.write('''
**Reduces soil erosion**: Contour rows slow runoff and reduce sheet and rill erosion; on suitable slopes, soil loss can be reduced by as much as 50%. \n
**Improves water infiltration**: Because water moves more slowly across the field, it has more time to enter the soil instead of running off. \n
**Increases soil moisture**: More infiltration and less runoff help the soil retain moisture, which can support crops during dry periods. \n
**Protects water quality**: Contour farming reduces sediment, nutrients, and pesticides carried by runoff into streams, rivers, and other surface waters. \n
**Preserves fertile topsoil**: By keeping valuable topsoil on sloping fields, it helps maintain long-term soil fertility and productivity. \n
**Reduces flood and landslide impacts**: Contour ploughing can lessen damage from heavy rain, storms, and landslides by controlling runoff. \n
**Low-cost conservation method**: It mainly requires planning the direction of ploughing and planting, making it a relatively low-cost and low-maintenance practice. 

        ''')
