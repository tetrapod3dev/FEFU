import axios from "axios";
import SERVER from "@/api/api";

export const mixinUploadImage = {
  methods: {
    async uploadImage(images) {
      let configs = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      let file = images;
      let formData = new FormData();
      formData.append("file", file);

      return await axios.post(
        SERVER.URL + SERVER.ROUTES.images.upload,
        formData,
        configs
      );
    },
  },
};
