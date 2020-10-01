package com.cloud.domain;

public class PageDto {

	private int curPage;
	private int perPageNum;
	private int totalCount;
	private int startPage;
	private int endPage;
	private boolean prev;
	private boolean next;
	private int displayPageNum = 5;
	private int startIndex;

	private void calcData() {
		endPage = (int) (Math.ceil(curPage / (double) displayPageNum) * displayPageNum);

		startPage = (endPage - displayPageNum) + 1;
		if (startPage <= 0) {
			startPage = 1;
		}

		int tempEndPage = (int) (Math.ceil(totalCount / (double) perPageNum));
		if (endPage > tempEndPage) {
			endPage = tempEndPage;
		}

		prev = startPage == 1 ? false : true;
		next = endPage * perPageNum < totalCount ? true : false;

		startIndex = (curPage - 1) * perPageNum;
	}

	public PageDto() {
		this.curPage = 1;
		this.perPageNum = 12;
	}

	public PageDto(int curPage) {
		this.curPage = curPage;
		this.perPageNum = 12;
	}

	public PageDto(int curPage, int perPageNum) {
		this.curPage = curPage;
		this.perPageNum = perPageNum;
	}

	public int getTotalCount() {
		return totalCount;
	}

	public void setTotalCount(int totalCount) {
		this.totalCount = totalCount;
		calcData();
	}

	public int getCurPage() {
		return curPage;
	}

	public void setCurPage(int curPage) {
		this.curPage = curPage;
	}

	public int getPerPageNum() {
		return perPageNum;
	}

	public void setPerPageNum(int perPageNum) {
		this.perPageNum = perPageNum;
	}

	public int getStartPage() {
		return startPage;
	}

	public void setStartPage(int startPage) {
		this.startPage = startPage;
	}

	public int getEndPage() {
		return endPage;
	}

	public void setEndPage(int endPage) {
		this.endPage = endPage;
	}

	public boolean isPrev() {
		return prev;
	}

	public void setPrev(boolean prev) {
		this.prev = prev;
	}

	public boolean isNext() {
		return next;
	}

	public void setNext(boolean next) {
		this.next = next;
	}

	public int getDisplayPageNum() {
		return displayPageNum;
	}

	public void setDisplayPageNum(int displayPageNum) {
		this.displayPageNum = displayPageNum;
	}

	public int getStartIndex() {
		return startIndex;
	}

	public void setStartIndex(int startIndex) {
		this.startIndex = startIndex;
	}

}