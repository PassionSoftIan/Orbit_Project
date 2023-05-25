<template>
<div>
  <div v-if="!isupdate">
    <p>대댓글 작성자 : {{comment.user.nick_name}}</p>
    <p>{{comment.content}}</p>
    <div v-if="comment.user.id === accounts.pk">
            <button @click="is_update">수정하기</button>
            <button @click="update_or_delete('delete')">삭제하기</button>
    </div>
  </div>
  <div v-if="isupdate">
        <input type="text" v-model="content">
        <button @click="update_or_delete('put')">저장하기</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name:"CommentRead",
    props:{
        comment:Object,
        accounts:Object
    },
    computed:{
        Token(){
            return this.$store.state.Token
        }
    },
    data(){
        return{
            content:this.comment.content,
            isupdate:false
        }
    },
    methods:{
        is_update(){
            this.isupdate = true
        },
        update_or_delete(method__){
            const update_url = `http://127.0.0.1:8000/api/v1/comment/detail/${this.comment.id}/`
            console.log("수정이나 삭제")

            axios({
                url:update_url,
                method:method__,
                headers:{
                    Authorization: `Token ${this.Token}`
                },
                data:{
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