<template>
  <div>
    <p>작성자 : {{review.user.nick_name}}</p>
    <div v-if="!isupdate">
        <p>평  점 : {{review.vote}}</p>
        <p v-if="review.content">내용 : {{review.content}}</p>
        <span>좋아요 : {{review.liked_user.length}}   </span>
        <button @click="like_fun">{{like}}</button>
        <div v-if="review.user.id === accounts.pk">
            <button @click="is_update">수정하기</button>
            <button @click="update_or_delete('delete')">삭제하기</button>
        </div>
        <br>
        <br>
        <CommentReadVue v-for="(comment, index) of this.comments" :key="index" :comment="comment" :accounts="accounts" @reload="get_comment"/>
        <input type="text" v-model="comment_input">
        <button @click="create_comment">작성</button>
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
import CommentReadVue from './CommentRead.vue'
export default {
    name:"ReadReview",
    components: {
        CommentReadVue
    },
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

            comments:null,
            comment_input:"",
            
            isupdate: false,
            like: "좋아요",
            like_method: "POST"
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
        like_fun(){
            if(this.review.user.id === this.accounts.pk){
                alert('자신의 글에는 좋아요를 할 수 없습니다.')
                return
            }

            axios({
                url:`http://127.0.0.1:8000/myaccounts/like/${this.review.id}/`,
                method:this.like_method,
                headers:{
                    Authorization: `Token ${this.Token}`
                },
            })
            .then((res) => {
                console.log(res)
                this.$emit('like')
                if(this.like === "좋아요"){
                    this.like = "좋아요 취소"
                    this.like_method = "DELETE"
                }
                else{
                    this.like = "좋아요"
                    this.like_method = "POST"
                }
            })
            .catch((err)=>{
                console.log(err)

            })
        },
        is_like(){
            for(let liked_user of this.review.liked_user)
            {
                if (liked_user.id === this.accounts.pk){
                    this.like = "좋아요 취소"
                    this.like_method = "DELETE"
                    return
                }
            }
            this.like = "좋아요"
            this.like_method = "POST"
            return
        },
        get_comment(){
            axios({
                method:'GET',
                url:`http://127.0.0.1:8000/api/v1/comment/${this.review.id}/`,
                headers:{
                    Authorization: `Token ${this.Token}`
                },
            })
            .then((res)=>{
                console.log(res)
                this.comments = res.data
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        create_comment(){
            if(this.comment_input === ""){
                alert('내용을 입력해 주세요')
                return
            }
            axios({
                method:'POST',
                url:`http://127.0.0.1:8000/api/v1/comment/${this.review.id}/`,
                headers:{
                    Authorization: `Token ${this.Token}`
                },
                data:{
                    content: this.comment_input
                }
            })
            .then((res)=>{
                console.log(res)
                this.comment_input = ""
                this.get_comment()
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    },
    created(){
        this.is_like()
        this.get_comment()

    }



}
</script>

<style>

</style>