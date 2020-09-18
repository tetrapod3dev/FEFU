package com.cloud.controller;

import java.io.IOException;

import javax.servlet.http.HttpServletRequest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.cloud.domain.FileUploadDto;
import com.cloud.service.FileUploadService;

import io.swagger.annotations.ApiOperation;

@RestController
public class FileController {

	private static final Logger logger = LoggerFactory.getLogger(FileController.class);

	@Autowired
	private FileUploadService fileService;

	@ApiOperation(value = "파일 업로드", response = FileUploadDto.class)
	@PostMapping(value = "/upload")
	public ResponseEntity<FileUploadDto> uploadFile(@RequestParam("file") MultipartFile file) {
		String fileName = "";
		String fileDownloadUri = "";

		try {
			fileName = fileService.saveFile(file);
			fileDownloadUri = ServletUriComponentsBuilder.fromCurrentContextPath().path("/file/download/").path(fileName)
					.toUriString();
			FileUploadDto data = new FileUploadDto(fileName, fileDownloadUri, file.getContentType(), file.getSize());
			return new ResponseEntity<FileUploadDto>(data, HttpStatus.OK);
		} catch (Exception e) {
			logger.error(e.getMessage());
		}
		return null;
	}

	@ApiOperation(value = "파일 다운로드")
	@GetMapping("/download/{fileName:.+}")
	public ResponseEntity<Resource> downloadFile(@PathVariable String fileName, HttpServletRequest request) {
		Resource resource = fileService.loadFile(fileName);
		String contentType = null;
		try {
			contentType = request.getServletContext().getMimeType(resource.getFile().getAbsolutePath());
		} catch (IOException e) {
			logger.error(e.getMessage());
		}

		if (contentType == null) {
			contentType = "application/octet-stream";
		}

		return ResponseEntity.ok().contentType(MediaType.parseMediaType(contentType))
				.header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + resource.getFilename() + "\"")
				.body(resource);
	}
}
