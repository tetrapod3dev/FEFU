package com.cloud.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.CampaignDto;
import com.cloud.service.CampaignService;

@RestController
public class CampaignController {

	private static final Logger logger = LoggerFactory.getLogger(CampaignController.class);
	
	@Autowired
	private CampaignService campaignService;
	
	@GetMapping(value = "/")
	public ResponseEntity<List<CampaignDto>> searchAll(
			@RequestParam("campaign_type") String campaignType,
			@RequestParam("type") String type,
			@RequestParam("content") String content,
			@RequestParam("page_no") int pageNo){
		List<CampaignDto> list = campaignService.findAll(campaignType, pageNo, type, content);
		list.forEach(el -> logger.info(el.getTitle() + "<<<<<<<<<<<<<<<<<<<<<<<<<"));
		return new ResponseEntity<List<CampaignDto>>(list, HttpStatus.OK);
	}
	
	@GetMapping(value = "/{campaign_no}")
	public ResponseEntity<CampaignDto> campaignDetail(@PathVariable("campaign_no") int no){
		CampaignDto dto = campaignService.findDetail(no);
		dto.setTag(campaignService.findTagByNo(no));
		return new ResponseEntity<CampaignDto>(dto, HttpStatus.OK);
	}
	
	@PostMapping(value = "/")
	public ResponseEntity<String> registCampaign(@RequestBody CampaignDto data){
		logger.info(data.getTitle() + "============");
		data.getTag().forEach(el -> logger.info(el + "================"));
		int res = campaignService.insertCampaign(data);
		if(res == 0) {
			return new ResponseEntity<String>("등록 실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("등록 성공", HttpStatus.OK);
	}
}
