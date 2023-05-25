<template>
  <div class="item">
    <div class="container">
        <span>작성자 :
            <span v-if="userCheck">
                <router-link :to="{name:'others',params:{userpk: review.user.id}}"> {{review.user.nick_name}} </router-link>
            </span>
            <span v-else>
                {{review.user.nick_name}}
            </span>
        </span>
    </div>
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
        <div>
        <button @click="reviewreview=!reviewreview" v-if="!reviewreview">대댓글 보기</button>
        <button @click="reviewreview=!reviewreview" v-if="reviewreview">대댓글 숨기기</button>
        <div v-if="reviewreview">
        <CommentReadVue v-for="(comment, index) of this.comments" :key="index" :comment="comment" :accounts="accounts" @reload="get_comment"/>
        <input type="text" v-model="comment_input">
        <button @click="create_comment" v-if="reviewreview">작성</button>
        </div>
        </div>
        <br>
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
        },
        userCheck(){
            if (this.review.user.id === this.$store.state.user_pk){
                return false
            }
            return true
        },
    },
    data(){
        return{
            content: this.review.content,
            vote: this.review.vote,

            comments:null,
            comment_input:"",
            
            isupdate: false,
            like: "좋아요",
            like_method: "POST",

            create: false,
            reviewreview: false
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
                return this.$store.dispatch('userChange')
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

<style scoped>
.item{
    border: solid;
    border-color: black;
}

.container {
    display: flex;
    flex-direction: row;
    justify-content: center;
}
* {
margin: 0;
padding: 0;
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
box-sizing: border-box;
}

a {
color: #03658c;
text-decoration: none;
}

ul {
list-style-type: none;
}

body {
font-family: 'Roboto', Arial, Helvetica, Sans-serif, Verdana;
background: #dee1e3;
}

/** ====================
* Lista de Comentarios
=======================*/
/* .comments-container {
margin: 60px auto 15px;
width: 768px;
} */

.comments-container h1 {
font-size: 36px;
color: #283035;
font-weight: 400;
}

.comments-container h1 a {
font-size: 18px;
font-weight: 700;
}

.comments-list {
margin-top: 30px;
position: relative;
}

/**
* Lineas / Detalles
-----------------------*/
.comments-list:before {
content: '';
width: 2px;
height: 100%;
background: #c7cacb;
position: absolute;
left: 32px;
top: 0;
}

.comments-list:after {
content: '';
position: absolute;
background: #c7cacb;
bottom: 0;
left: 27px;
width: 7px;
height: 7px;
border: 3px solid #dee1e3;
-webkit-border-radius: 50%;
-moz-border-radius: 50%;
border-radius: 50%;
}

.reply-list:before, .reply-list:after {display: none;}
.reply-list li:before {
content: '';
width: 60px;
height: 2px;
background: #c7cacb;
position: absolute;
top: 25px;
left: -55px;
}


.comments-list li {
margin-bottom: 15px;
display: block;
position: relative;
}

.comments-list li:after {
content: '';
display: block;
clear: both;
height: 0;
width: 0;
}

.reply-list {
padding-left: 88px;
clear: both;
margin-top: 15px;
}
/**
* Avatar
---------------------------*/
.comments-list .comment-avatar {
width: 65px;
height: 65px;
position: relative;
z-index: 99;
float: left;
border: 3px solid #FFF;
-webkit-border-radius: 4px;
-moz-border-radius: 4px;
border-radius: 4px;
-webkit-box-shadow: 0 1px 2px rgba(0,0,0,0.2);
-moz-box-shadow: 0 1px 2px rgba(0,0,0,0.2);
box-shadow: 0 1px 2px rgba(0,0,0,0.2);
overflow: hidden;
}

.comments-list .comment-avatar img {
width: 100%;
height: 100%;
}

.reply-list .comment-avatar {
width: 50px;
height: 50px;
}

.comment-main-level:after {
content: '';
width: 0;
height: 0;
display: block;
clear: both;
}
/**
* Caja del Comentario
---------------------------*/
.comments-list .comment-box {
width: 680px;
float: right;
position: relative;
-webkit-box-shadow: 0 1px 1px rgba(0,0,0,0.15);
-moz-box-shadow: 0 1px 1px rgba(0,0,0,0.15);
box-shadow: 0 1px 1px rgba(0,0,0,0.15);
}

.comments-list .comment-box:before, .comments-list .comment-box:after {
content: '';
height: 0;
width: 0;
position: absolute;
display: block;
border-width: 10px 12px 10px 0;
border-style: solid;
border-color: transparent #FCFCFC;
top: 8px;
left: -11px;
}

.comments-list .comment-box:before {
border-width: 11px 13px 11px 0;
border-color: transparent rgba(0,0,0,0.05);
left: -12px;
}

.reply-list .comment-box {
width: 610px;
}
.comment-box .comment-head {
background: #FCFCFC;
padding: 10px 12px;
border-bottom: 1px solid #E5E5E5;
overflow: hidden;
-webkit-border-radius: 4px 4px 0 0;
-moz-border-radius: 4px 4px 0 0;
border-radius: 4px 4px 0 0;
}

.comment-box .comment-head i {
float: right;
margin-left: 14px;
position: relative;
top: 2px;
color: #A6A6A6;
cursor: pointer;
-webkit-transition: color 0.3s ease;
-o-transition: color 0.3s ease;
transition: color 0.3s ease;
}

.comment-box .comment-head i:hover {
color: #03658c;
}

.comment-box .comment-name {
color: #283035;
font-size: 14px;
font-weight: 700;
float: left;
margin-right: 10px;
}

.comment-box .comment-name a {
color: #283035;
}

.comment-box .comment-head span {
float: left;
color: #999;
font-size: 13px;
position: relative;
top: 1px;
}

.comment-box .comment-content {
background: #FFF;
padding: 12px;
font-size: 15px;
color: #595959;
-webkit-border-radius: 0 0 4px 4px;
-moz-border-radius: 0 0 4px 4px;
border-radius: 0 0 4px 4px;
}

.comment-box .comment-name.by-author, .comment-box .comment-name.by-author a {color: #03658c;}
.comment-box .comment-name.by-author:after {
content: 'autor';
background: #03658c;
color: #FFF;
font-size: 12px;
padding: 3px 5px;
font-weight: 700;
margin-left: 10px;
-webkit-border-radius: 3px;
-moz-border-radius: 3px;
border-radius: 3px;
}

/** =====================
* Responsive
========================*/
@media only screen and (max-width: 766px) {
.comments-container {
  width: 480px;
}

.comments-list .comment-box {
  width: 390px;
}

.reply-list .comment-box {
  width: 320px;
}
}
</style>