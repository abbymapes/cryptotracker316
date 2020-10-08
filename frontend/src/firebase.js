import { firebaseConfig } from './firebaseConfig'
export async function firestore() {
    if (process.browser) {
        return window.db
    } else {
        const firebase = await import('firebase')
        if (firebase.apps.length == 0) {
            let app = firebase.initializeApp(firebaseConfig)
            return app.firestore()
        }
        else {
            return firebase.apps[0].firestore()
        }
    }
}

export async function auth() {
    if (process.browser) {
        return window.au
    } else {
        const firebase = await import('firebase')
        if (firebase.apps.length == 0) {
            let app = firebase.initializeApp(firebaseConfig)
            return app.auth()
        }
        else {
            return firebase.apps[0].auth()
        }
    }
}

