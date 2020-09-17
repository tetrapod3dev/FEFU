package com.cloud.service;

import java.io.File;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import com.cloud.domain.FileProperties;
import com.cloud.exception.FileException;

@Service
public class FileUploadService {

	private final Path fileLocation;

	@Autowired
	public FileUploadService(FileProperties properties) {
		this.fileLocation = Paths.get(properties.getUploadDir()).toAbsolutePath().normalize();
		try {
			Files.createDirectories(this.fileLocation);
		} catch (Exception e) {
			throw new FileException("디렉토리 생성 실패");
		}
	}

	public String saveFile(MultipartFile file) {
		String fileName = StringUtils.cleanPath(file.getOriginalFilename());
		String fileExtension = fileName.substring(fileName.lastIndexOf("."));
		String saveName = UUID.randomUUID().toString().concat(fileExtension);

		try {
			Path targetLocation = this.fileLocation.resolve(saveName);
			File tempFile = new File(targetLocation.toString());
			file.transferTo(tempFile);
			return saveName;
		} catch (Exception e) {
			throw new FileException("파일 업로드 실패");
		}
	}

	public Resource loadFile(String fileName) {
		try {
			Path filePath = this.fileLocation.resolve(fileName).normalize();
			Resource resource = new UrlResource(filePath.toUri());

			if (resource.exists()) {
				return resource;
			} else {
				throw new FileException("파일 찾을 수 없음");
			}
		} catch (MalformedURLException e) {
			throw new FileException("URL 에러");
		}

	}
}
