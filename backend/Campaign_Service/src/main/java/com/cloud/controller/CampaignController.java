package com.cloud.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
import com.cloud.domain.PageDto;
import com.cloud.service.CampaignService;

@RestController
public class CampaignController {

	private static final Logger logger = LoggerFactory.getLogger(CampaignController.class);

	@Autowired
	private CampaignService campaignService;

	@GetMapping(value = "/")
	public ResponseEntity<Map<String, Object>> searchAll(@RequestParam("campaign_type") String campaignType,
			@RequestParam("type") String type, @RequestParam("content") String content,
			@RequestParam("page_no") int pageNo) {
		int totalCount = campaignService.findByCount(campaignType, pageNo, type, content);
		PageDto page = new PageDto();
		page.setTotalCount(totalCount);

		List<CampaignDto> list = campaignService.findAll(campaignType, pageNo, type, content, page.getStartIndex(),
				page.getPerPageNum());
		Map<String, Object> data = new HashMap<String, Object>();
		data.put("list", list);
		data.put("page", page);
		return new ResponseEntity<Map<String, Object>>(data, HttpStatus.OK);
	}

	@GetMapping(value = "/{campaign_no}")
	public ResponseEntity<Map<String, Object>> campaignDetail(@PathVariable("campaign_no") int no) {
		Map<String, Object> list = campaignService.findDetail(no);
		return new ResponseEntity<Map<String, Object>>(list, HttpStatus.OK);
	}

	@PostMapping(value = "/")
	public ResponseEntity<String> registCampaign(@RequestBody Map<String, Object> data) {
		int res = campaignService.insertCampaign(data);

		if(res == 0) {
			return new ResponseEntity<String>("등록 실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("등록 성공", HttpStatus.OK);
	}
}
