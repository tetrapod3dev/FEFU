import axios from "axios";
import SERVER from "@/api/api";

export const imageUploadable = {
  methods: {
    async uploadImage(images) {
      let photo = "";
      let configs = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      let file = images;
      let formData = new FormData();
      formData.append("file", file);

      await axios
        .post(SERVER.URL + SERVER.ROUTES.images.upload, formData, configs)
        .then((res) => {
          photo = res.data.fileName;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
      return photo;
    },
  },
};
