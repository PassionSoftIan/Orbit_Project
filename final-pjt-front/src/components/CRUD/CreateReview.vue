<template>
  <div>
    <p>CreateReview page</p>

    <input type="text" v-model="content">
    <input type="range" name="vote" min="0.5" max="5" step="0.5" v-model="vote">
    <span>{{vote}}</span>
    <button @click="submit">submit</button>



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
        }
    },
    props: {
        movie_id: String
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
                    content:this.content
                }
            })
            .then((res)=>{
                res
                this.content = ""
                this.vote = 0
                this.$emit("created")

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

<style>

</style>