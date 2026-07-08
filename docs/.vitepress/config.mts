import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Jospy UI",
  description: "A premium, modern, and highly customizable UI library for Roblox exploit scripts.",
  base: '/JospyUI/',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Documentation', link: '/guide/getting-started' }
    ],

    sidebar: [
      {
        text: 'Introduction',
        items: [
          { text: 'Getting Started', link: '/guide/getting-started' }
        ]
      },
      {
        text: 'Components',
        items: [
          { text: 'Elements', link: '/guide/elements' },
          { text: 'Advanced Features', link: '/guide/advanced' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ijosephyusufk-dev/JospyUI' }
    ],

    search: {
      provider: 'local'
    }
  },
  appearance: 'dark'
})
