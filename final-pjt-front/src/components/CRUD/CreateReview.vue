<template>
  <div>
    <p>CreateReview page</p>
    <button @click="create=!create" v-if="!create">게시글 작성</button>
    <div v-if="this.create">
    <input type="text" v-model="content" @keydown.enter="submit">
    <!-- <input type="range" name="vote" min="0.5" max="5" step="0.5" v-model="vote"> -->
    <button @click="submit">submit</button>
    <button @click='create=!create'>취소</button>
    <h1></h1>
    <fieldset class="rating">
    <input type="radio" id="star5" name="rating" value="5" v-model="vote"/><label class = "full" for="star5" title="Awesome - 5 stars"></label>
    <input type="radio" id="star4half" name="rating" value="4.5" v-model="vote"/><label class="half" for="star4half" title="Pretty good - 4.5 stars"></label>
    <input type="radio" id="star4" name="rating" value="4" v-model="vote"/><label class = "full" for="star4" title="Pretty good - 4 stars"></label>
    <input type="radio" id="star3half" name="rating" value="3.5" v-model="vote"/><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
    <input type="radio" id="star3" name="rating" value="3" v-model="vote"/><label class = "full" for="star3" title="Meh - 3 stars"></label>
    <input type="radio" id="star2half" name="rating" value="2.5" v-model="vote"/><label class="half" for="star2half" title="Kinda bad - 2.5 stars"></label>
    <input type="radio" id="star2" name="rating" value="2" v-model="vote"/><label class = "full" for="star2" title="Kinda bad - 2 stars"></label>
    <input type="radio" id="star1half" name="rating" value="1.5" v-model="vote"/><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
    <input type="radio" id="star1" name="rating" value="1" v-model="vote"/><label class = "full" for="star1" title="Sucks big time - 1 star"></label>
    <input type="radio" id="starhalf" name="rating" value="0.5" v-model="vote"/><label class="half" for="starhalf" title="Sucks big time - 0.5 stars"></label>
    </fieldset>
    <span style="margin: 10px">{{vote}}</span>
    </div>


  </div>
</template>

<script>
import axios from "axios"
export default {
    name: "CreateReview",
    computed:{
        Token(){
            return this.$store.state.Token
        }
    },
    data(){
        return {
            content:"",
            vote:0,
            create:false
        }
    },
    props: {
        movie_id: String,
        accounts: Object
    },
    methods:{
        submit(){
            const post_url = `http://127.0.0.1:8000/api/v1/review/${this.movie_id}/`
            axios({
                url:post_url,
                method:"POST",
                headers:{
                    Authorization: `Token ${this.Token}`
                },
                data:{
                    vote: this.vote,
                    content:this.content,
                }
            })
            .then((res)=>{
                res
                this.content = ""
                this.vote = 0
                this.$emit("created")
            return this.$store.dispatch('userChange')
            })
            
            .catch((err)=>{
                console.log(err)
                this.content = ""
                this.vote = 0
            })
        }

    }

}
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

fieldset, label { margin: 0; padding: 0; }
body{ margin: 20px; }
h1 { font-size: 1.5em; margin: 10px; }

/****** Style Star Rating Widget *****/

.rating { 
  border: none;
  display: inline-block;
}

.rating > input { display: none; } 
.rating > label:before { 
  margin: 5px;
  font-size: 1.25em;
  font-family: FontAwesome;
  display: inline-block;
  content: "\f005";
}

.rating > .half:before { 
  content: "\f089";
  position: absolute;
}

.rating > label { 
  color: #ddd; 
 float: right; 
}

/***** CSS Magic to Highlight Stars on Hover *****/

.rating > input:checked ~ label, /* show gold star when clicked */
.rating:not(:checked) > label:hover, /* hover current star */
.rating:not(:checked) > label:hover ~ label { color: #FFD700;  } /* hover previous stars in list */

.rating > input:checked + label:hover, /* hover current star when changing rating */
.rating > input:checked ~ label:hover,
.rating > label:hover ~ input:checked ~ label, /* lighten current selection */
.rating > input:checked ~ label:hover ~ label { color: #FFED85;  } 
</style>