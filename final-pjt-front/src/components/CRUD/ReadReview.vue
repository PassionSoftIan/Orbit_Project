<template>
  <div>
    <p>작성자 : {{review.username}}</p>
    <div v-if="!isupdate">
        <p>평  점 : {{review.vote}}</p>
        <p v-if="review.content">내용 : {{review.content}}</p>
        <div v-if="review.user === accounts.pk">
            <button @click="is_update">수정하기</button>
            <button @click="update_or_delete('delete')">삭제하기</button>
        </div>
    </div>
    <div v-if="isupdate">
        <span>평  점 : </span>
        <span>{{vote}}</span>
        <input type="range" name="vote" min="0.5" max="5" step="0.5" v-model="vote">
        <br>
        <span>내용 : </span>
        <input type="text" v-model="content">
        <button @click="update_or_delete('put')">저장하기</button>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from "axios"
export default {
    name:"ReadReview",
    props:{
        review:Object,
        accounts:Object,
    },
    computed:{
        Token(){
            return this.$store.state.Token
        }
    },
    data(){
        return{
            content: this.review.content,
            vote: this.review.vote,
            
            isupdate: false,
        }
    },
    methods:{
        is_update(){
            this.isupdate = true
            this.$emit("want_update")
        },
        update_or_delete(method__){
            const update_url = `http://127.0.0.1:8000/api/v1/review/detail/${this.review.id}/`

            axios({
                url:update_url,
                method:method__,
                headers:{
                    Authorization: `Token ${this.Token}`
                },
                data:{
                    vote: this.vote,
                    content: this.content
                }

            })
            .then((res)=>{
                console.log(res)
                this.isupdate = false
                this.$emit("reload")

            })
            .catch((err)=>{
                this.isupdate = false
                console.log(err)
            })

        },
    }



}
</script>

<style>

</style>