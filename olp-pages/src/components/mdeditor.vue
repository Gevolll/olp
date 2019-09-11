<template lang="html">
  <div class="md-editor-wrap">
    <link rel="stylesheet" href="/static/editor.md/css/editormd.min.css">
    <link rel="stylesheet" :href="'/static/editor.md/css/codeTheme/'+codeTheme">
    <div :id="editorId"></div>
  </div>
</template>

<script>
import scriptjs from 'scriptjs';
import { defaultConfig, codeThemes } from '../../config/editor.md';

export default {
  name: 'EditorMd',
  props: {
    editorId: {
      type: String,
      default: 'markdown-editor',
    },
    onchange: { // 内容改变时回调，返回 (html, markdown, text)
      type: Function
    },
    config: { // 编辑器配置
      type: Object
    },
    codeTheme: {  // 代码高亮主题
      type: String,
      default: 'vibrant-ink.min.css'
    },
    initData: {
      type: String
    },
    initDataDelay: {
      type: Number,
      default: 0
    },
    isView: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      editor: null,
      codeThemes,
      editorLoaded: false
    }
  },
  methods: {
    fetchScript: function (url) {
      return new Promise((resolve) => {
        scriptjs(url, () => {
          resolve();
        });
      });
    },
    getConfig: function () {
      return {...defaultConfig, ...this.config}
    },
    initEditor: function () {
      (async () => {
        await this.fetchScript('/static/editor.md/jquery.min.js');
        await this.fetchScript('/static/editor.md/editormd.min.js');

        this.$nextTick(() => {
          let editor = window.editormd(this.editorId, this.getConfig());

          editor.on('load', () => {
            setTimeout(() => {
              this.editorLoaded = true;
              this.initData && editor.setMarkdown(this.initData);
            }, this.initDataDelay);
          });

          this.onchange && editor.on('change', () => {
            let html = editor.getPreviewedHTML();

            this.onchange({
              markdown: editor.getMarkdown(),
              html: html,
              text: window.$(html).text()
            });
          });

          this.editor = editor;
        });
      })();
    }
  },
  mounted () {
    // this.initEditor();
  },
  watch: {
    initData: function (newVal) {
      if (newVal) {
        this.editorLoaded && this.editor.setMarkdown(newVal);
      }
    },
    isView: function (newVal) {
      if (newVal) {
        this.initEditor();
      }
    }
  }
}
</script>

<style lang="css">
</style>
