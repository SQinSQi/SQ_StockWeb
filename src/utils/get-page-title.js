import defaultSettings from '@/settings'

const title = defaultSettings.title || 'Wet Snow Long Hill'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
