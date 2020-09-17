package com.cloud.domain;

public class FileProperties {

	private String uploadDir;

	public FileProperties() {
//		this.uploadDir = "C:\\Users\\multicampus\\Documents\\tmp";
		this.uploadDir = "/tmp";
	}

	public String getUploadDir() {
		return uploadDir;
	}

	public void setUploadDir(String uploadDir) {
		this.uploadDir = uploadDir;
	}

}
