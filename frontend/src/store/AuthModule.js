import * as firebase from "firebase/app";
import "firebase/auth";
import "firebase/database";

export default {
  namespaced: true,
  state: {
    user: null,
  },
  getters: {
    USER(state) {
      return state.user;
    },
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
      const userListRef = firebase.database().ref("presence");
      const myUserRef = userListRef.push();

      firebase
        .database()
        .ref(".info/connected")
        .on("value", function(snap) {
          if (snap.val()) {
            // if we lose network then remove this user from the list
            myUserRef.onDisconnect().remove();
            // set user's online status
            let presenceObject = { user: payload, status: "online" };
            myUserRef.set(presenceObject);
          } else {
            // client has lost network
            let presenceObject = { user: payload, status: "offline" };
            myUserRef.set(presenceObject);
          }
        });
    },
  },
  actions: {
    signUserUp({ commit }, payload) {
      commit("setLoading", true, { root: true });
      commit("clearError", null, { root: true });
      firebase
        .auth()
        .createUserWithEmailAndPassword(payload.email, payload.password)
        .then((auth) => {
          firebase
            .database()
            .ref("users")
            .child(auth.user.uid)
            .set({
              name: payload.username,
            })
            .then(() => {
              commit("setLoading", false, { root: true });
              const newUser = {
                id: auth.user.uid,
                username: payload.username,
              };
              commit("setUser", newUser);
            })
            .catch((error) => {
              commit("setLoading", false, { root: true });
              commit("setError", error, { root: true });
            });
        })
        .catch((error) => {
          commit("setLoading", false, { root: true });
          commit("setError", error, { root: true });
        });
    },
    signUserIn({ commit }, payload) {
      commit("setLoading", true, { root: true });
      commit("clearError", null, { root: true });
      firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then((auth) => {
          firebase
            .database()
            .ref("users")
            .child(auth.user.uid)
            .once("value", function() {
              commit("setLoading", false, { root: true });
              const newUser = {
                id: auth.user.uid,
                username: auth.user.email,
              };
              commit("setUser", newUser);
            });
        })
        .catch((error) => {
          commit("setLoading", false, { root: true });
          commit("setError", error, { root: true });
        });
    },
  },
};
