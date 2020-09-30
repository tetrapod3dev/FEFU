package com.cloud.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.CampaignDto;
import com.cloud.domain.PageDto;
import com.cloud.service.CampaignService;

import io.swagger.annotations.ApiOperation;
import springfox.documentation.annotations.ApiIgnore;

@RestController
public class CampaignController {

	private static final Logger logger = LoggerFactory.getLogger(CampaignController.class);

	@Autowired
	private CampaignService campaignService;

	@ApiOperation(value = "캠페인 목록 검색")
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

	@ApiOperation(value = "캠페인 상세 정보")
	@GetMapping(value = "/{campaign_no}")
	public ResponseEntity<Map<String, Object>> campaignDetail(@PathVariable("campaign_no") int no) {
		Map<String, Object> list = campaignService.findDetail(no);
		return new ResponseEntity<Map<String, Object>>(list, HttpStatus.OK);
	}

	@ApiOperation(value = "모든 타입별 캠페인 등록")
	@PostMapping(value = "/")
	public ResponseEntity<String> registCampaign(@RequestBody Map<String, Object> data) {
		int res = campaignService.insertCampaign(data);

		if (res == 0) {
			return new ResponseEntity<String>("등록 실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("등록 성공", HttpStatus.OK);
	}

	@ApiOperation(value = "해당 유저가 생성한 캠페인 목록 가져오기")
	@GetMapping(value = "/my-campaign")
	public ResponseEntity<List<CampaignDto>> getRegistCampaign(@ApiIgnore @RequestHeader("X-USERNAME") String username) {
		List<CampaignDto> list = campaignService.findByRegistCampaign(username);
		return new ResponseEntity<List<CampaignDto>>(list, HttpStatus.OK);
	}
	
	@ApiOperation(value = "해당 유저 캠페인 참석 여부 확인")
	@GetMapping(value = "/join/{campaign_no}")
	public ResponseEntity<Boolean> checkJoin(@ApiIgnore @RequestHeader("X-USERNAME") String username,
			@PathVariable("campaign_no") int no) {
		int res = campaignService.checkJoin(no, username);
		if (res == 0) {
			return new ResponseEntity<Boolean>(false, HttpStatus.OK);
		}
		return new ResponseEntity<Boolean>(true, HttpStatus.OK);
	}

	@ApiOperation(value = "해당 유저 참여 캠페인 목록 가져오기")
	@GetMapping(value = "/join")
	public ResponseEntity<List<CampaignDto>> checkJoinList(@ApiIgnore @RequestHeader("X-USERNAME") String username) {
		List<CampaignDto> list = campaignService.findByJoinCampaign(username);
		return new ResponseEntity<List<CampaignDto>>(list, HttpStatus.OK);
	}
	
	@ApiOperation(value = "해당 캠페인 참석 하기")
	@PostMapping(value = "/join")
	public ResponseEntity<String> joinCampaign(@ApiIgnore @RequestHeader("X-USERNAME") String username,
			@RequestBody Map<String, Integer> map) {
		int no = map.get("campaign_no");
		int res = campaignService.joinCampaign(no, username);
		if (res == 0) {
			return new ResponseEntity<String>("fail", HttpStatus.OK);
		}
		return new ResponseEntity<String>("success", HttpStatus.OK);
	}

	@ApiOperation(value = "캠페인 나가기")
	@DeleteMapping(value = "/leave/{campaign_no}")
	public ResponseEntity<String> leaveCampaign(@ApiIgnore @RequestHeader("X-USERNAME") String username,
			@PathVariable("campaign_no") int no) {
		int res = campaignService.leaveCampaign(no, username);
		if (res == 0) {
			return new ResponseEntity<String>("fail", HttpStatus.OK);
		}
		return new ResponseEntity<String>("success", HttpStatus.OK);
	}
}
