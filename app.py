import streamlit as st
import pickle
import streamlit.components.v1 as components

courses = pickle.load(open("dataset_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

logo_html = """
    <img src="https://cdn.discordapp.com/attachments/1275135058855854243/1284110709856403467/output-onlinepngtools.png?ex=66e570ca&is=66e41f4a&hm=734c6a97b22c57c2d1f584f99754eded6b51dcc7887277487eea6fcc5651c473&" alt="Platform Logo" style="position: absolute; top: 10px; left: 10px; width: 180px; height: auto;">
"""

components.html(logo_html, height=110)


page_bg_color = """
<style>
body {
    background-color: #99a3a4;  
}

.main {
    background-color: #99a3a4;  
}

</style>
"""

st.markdown(page_bg_color, unsafe_allow_html=True)


carousel_html = """
<style>
.carousel {
  position: relative;
  overflow: hidden;
  width: 100%;
  margin-bottom: -50px; 
}

.carousel-container {
  display: flex;
  width: 100%;
  transition: transform 0.5s ease-in-out;
}

.carousel img {
  width: calc(100% / 3 - 20px); 
  height: auto;
  flex-shrink: 0;
  margin: 0 5px; 
  max-height: 400px; 
}

.carousel-controls {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
}

.carousel-control {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 10px;
  cursor: pointer;
}
</style>

<div class="carousel">
  <div class="carousel-container">
    <!-- Images will be dynamically inserted here by JavaScript -->
  </div>
  <div class="carousel-controls">
    <div class="carousel-control" id="prev">‹</div>
    <div class="carousel-control" id="next">›</div>
  </div>
</div>

<script>
const images = [
  "https://www.keystonesubic.com/storage/2023/03/web-devlopment.jpg",
  "https://s3.amazonaws.com/mobileappdaily/mad/uploads/mad_blog_5e834bdc69de51585662940.png",
  "https://www.michaelpage.ae/sites/michaelpage.ae/files/legacy/7_digital_skills600x387.png",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM7tvY0i8xuYalija0O2iSFP0GvWhG2H-uOQ&s",
  "https://images.pexels.com/photos/1264210/pexels-photo-1264210.jpeg?cs=srgb&dl=pexels-andre-furtado-43594-1264210.jpg&fm=jpg",
  "https://storage.googleapis.com/website-production/uploads/2021/06/search-engine-marketing-best-practices.png",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvXFkY1gE3sfM712nyWj2LRj8DRO6_7MyiXw&s",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAxp095IBlY3mkY90PzA7b1k3tlGTGi2Kg_A&s",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwUmXnBstefvlxEtwnGWirXN5SmaZxrH8ahQ&s",
  "https://miro.medium.com/v2/resize:fit:1192/1*jXusXvCfxECPU_Jh9S_E3w.jpeg"
];


const carouselContainer = document.querySelector('.carousel-container');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

function createCarouselItems() {
  images.forEach((src) => {
    const img = document.createElement('img');
    img.src = src;
    carouselContainer.appendChild(img);
  });

  carouselContainer.insertAdjacentHTML('afterbegin', carouselContainer.lastElementChild.outerHTML);
  carouselContainer.insertAdjacentHTML('beforeend', carouselContainer.firstElementChild.outerHTML);
}

createCarouselItems();

const totalImages = images.length;
let index = 1; 

function showImage(index) {
  const offset = (index - 1) * (100 / (totalImages + 2));
  carouselContainer.style.transition = 'transform 0.5s ease-in-out';
  carouselContainer.style.transform = `translateX(-${offset}%)`;
}

nextButton.addEventListener('click', () => {
  if (index === totalImages + 1) {
    carouselContainer.style.transition = 'none'; 
    index = 1; 
    showImage(index);
    setTimeout(() => {
      carouselContainer.style.transition = 'transform 0.5s ease-in-out';
    }, 50);
  } else {
    index++;
    showImage(index);
  }
});

prevButton.addEventListener('click', () => {
  if (index === 0) {
    carouselContainer.style.transition = 'none';
    index = totalImages; 
    showImage(index);
    setTimeout(() => {
      carouselContainer.style.transition = 'transform 0.5s ease-in-out'; 
    }, 50);
  } else {
    index--;
    showImage(index);
  }
});
showImage(index);
</script>
"""

components.html(carousel_html, height=190)

st.header("Courses Recommendation")

courses_list = courses['Course'].values

selectvalue = st.selectbox("Select a course from the dropdown menu", courses_list)

def recommend(data):
    index = courses[courses['Course'] == data].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_course = []
    for i in distance[0:5]:
        recommend_course.append((courses.iloc[i[0]].Course, courses.iloc[i[0]].Link))  
    return recommend_course

if st.button("Show Recommendations"):
    course_recommendations = recommend(selectvalue)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"[{course_recommendations[0][0]}]({course_recommendations[0][1]})")
    with col2:
        st.markdown(f"[{course_recommendations[1][0]}]({course_recommendations[1][1]})")
    with col3:
        st.markdown(f"[{course_recommendations[2][0]}]({course_recommendations[2][1]})")
    with col4:
        st.markdown(f"[{course_recommendations[3][0]}]({course_recommendations[3][1]})")
    with col5:
        st.markdown(f"[{course_recommendations[4][0]}]({course_recommendations[4][1]})")


